import base64
#not yet ready
print("the string input requirement must be left blank only if you want to decode a file")
string = input("string: ")
if string =
path = input("file path: ")
def encode():
strtoen = string.encode("ascii")

enco = base64.b64encode(strtoen)

print(enco)

enco = base64.b64decode(enco)

print(enco)
