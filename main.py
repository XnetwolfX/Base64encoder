import base64
import os
def encodeit():
	string_path = input("string to encode or file path: ")
	print("if you choose Y that mean the program is going to treat it as a string, N mean like a path to a file or a file")
	path_or_string = input("string Y/N: ")
	if path_or_string == "Y" or "y":
		
		bytes = string_path.encode("ascii")
		print(bytes)
		enc = base64.b64encode(bytes)
		print(enc)
		
	elif path_or_string == "N" or "n":
		print("on testing Beta wait for upgrade")
		os.system("exit()")
		
option_1 = input("Do you want to encode or decode Y for encode and N for decode Y/N: ")
if option_1 == "Y" or "y":
	os.system("clear")
	print("encoding lab")
	encodeit()
elif option_1 == "N" or "n":
	os.system("clear")
	print("decoding lab")
	