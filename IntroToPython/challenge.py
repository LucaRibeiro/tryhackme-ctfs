import base64

file = open("D:\CTF\TryHackMe\IntroToPython\encodedflag.txt","r")
text = file.read()

for i in range(5):
    text = base64.b16decode(text)
for i in range(5):
    text = base64.b32decode(text)
for i in range(5):
    text = base64.b64decode(text)

print(text)