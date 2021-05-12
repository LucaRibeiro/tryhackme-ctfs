import base64

file = open('D://CTF//TryHackMe//Scripting//easy//b64.txt','r')
encoded_message = file.readline()
message = base64.b64decode(encoded_message)
for i in range(1, 50):
    message = base64.b64decode(message)

print(message)