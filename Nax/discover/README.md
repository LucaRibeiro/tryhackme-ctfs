# Apache
Apache/2.4.18 (Ubuntu) Server 

# Portas
PORT    STATE SERVICE  VERSION
- 22/tcp  open  ssh      OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
- 25/tcp  open  smtp     Postfix smtpd 8BITMIME, DSN, 
- 80/tcp  open  http     Apache httpd 2.4.18 ((Ubuntu))
- 389/tcp open  ldap     OpenLDAP 2.2.X - 2.3.X
- 443/tcp open  ssl/http Apache httpd 2.4.18 ((Ubuntu))
<br/><sup>[Full Scan Output](./nmap)</sup>

# Stego
Main page contains a stego challenge. <br/>
Elements -> Numbers in periodic table (ASCII) -> Text <br/>
``Ag - Hg - Ta - Sb - Po - Pd - Hg - Pt - Lr`` == 47 80 73 51 84 46 80 78 103 == /PI3T.PNg

http://10.10.10.5/PI3T.PNg

# Image
The image is a Piet image with credentials
``nagiosadmin:n3p3UQ&9BjLp4$7uhWdY``
