import base64
string = input("string: ")
strtoen = string.encode("ascii")

enco = base64.b64encode(strtoen)

print(enco)

enco = base64.b64decode(enco)

print(enco)