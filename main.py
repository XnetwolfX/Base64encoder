#import all requirements
import base64
#taking user input
in_file = input("where should it be saved?:" )
string = input("type your message:" )
#encoding function
def encode(in_file, string):
    file = open(in_file, "wb")
    en = encode(string)
    done = base64.b64encode(en)
    file.write(done)
    file.close()
#start encoding
encode(in_file, string)
