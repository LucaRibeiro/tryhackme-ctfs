# Intro To Python

## Task 1
### Section Complete
``No answer needed.``

## Task 2
### Section Complete
``No answer needed.``

## Task 3
### What is the name of >
``Greater than``
### What is the name of !=
``Not equal to``
### 1 != 0 will this return true or false (T or F)
``T``
### What is the name of <=
``Less than or equal to``
### Will this sample code return truee or false
``truee``
### Section Complete
``No answer needed.``

## Task 4
### Section Complete
``No answer needed.``

## Task 5
### What data type is 13
``integer``
### What data type is "65"
``string``
### What data type is 62.193
``float``
### Section Complete
``No answer needed.``

## Task 6
### Section Complete
``No answer needed.``

## Task 7
### Section Complete
``No answer needed.``

## Task 8
### Section Complete
``No answer needed.``

## Task 9
### Section Complete
``No answer needed.``

## Task 10
### Section Complete
``No answer needed.``

## Task 11
### Section Complete
``No answer needed.``

## Task 12
Code to encrypt the message:

```python
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
```