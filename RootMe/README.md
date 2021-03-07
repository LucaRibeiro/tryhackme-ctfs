# RootMe

## Recon
[Nmap](./recon/map) </br>
[Fuzzing](./recon/urls.json)
### Secret dir (found in css folder)
/panel

# Exploit
### Upload reverse shell
Use extension ".pHp5" to bypass blacklist filter and upload a [Web shell](./exploit/reverse.pHp5)

# Privesc
### Find SUID
find / -perm /4000 2>/dev/null

### Privesc
Run [exploit](./privesc/exploit)
