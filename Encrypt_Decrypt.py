import os
from dotenv import load_dotenv

load_dotenv()
fsadfsadfasd
def Encrypt_Decrypt(filepath, filename, fileextn, key):
    file = open(filepath + "/" + filename + "." + fileextn, "rb")
    data = file.read()
    file.close()
    bytedata = bytearray(data)
    for index, value in enumerate(bytedata):
        bytedata[index] = value ^ key

    file = open(filepath + "/" + filename + "." + fileextn, "wb")
    file.write(bytedata)
    file.close()

def main():
    filepath = os.getenv('encrypted_files')
    key = int(os.getenv('key'))
    file_items = os.listdir(filepath)

    for item in file_items:
        file_name, file_extn = item.split('.')
        Encrypt_Decrypt(filepath,file_name, file_extn, key)
        print('encrypted',item)

