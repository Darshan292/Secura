from cryptography.fernet import Fernet
from dotenv import load_dotenv
from dotenv import set_key
import os
import keyboard
import subprocess

load_dotenv()


def generatekey():
    return Fernet.generate_key()

def encrypt(filepath,filename, fileextn, key):
    cipher_suite = Fernet(key)
    with open(filepath + "/" + filename + "." + fileextn, "rb") as file:
        data = file.read()
        file.close
    encrypted_data=cipher_suite.encrypt(data)
    with open(filepath + "/" + filename + "." + fileextn, "wb") as file:
        file.write(encrypted_data)

def decrypt(filepath,filename, fileextn, vkey):
    cipher_suite = Fernet(vkey.encode('utf-8'))
    with open(filepath + "/" + filename + "." + fileextn, "rb") as file:
        data=file.read()
        file.close
    decrypted_data=cipher_suite.decrypt(data)
    with open(filepath + "/" + filename + "." + fileextn, "wb") as file:
        file.write(decrypted_data)
        
def encrdecr():
    
    filepath = os.getenv('encrypted_files')
    file_items = os.listdir(filepath)
    print("key for decreption: " + os.getenv("key"))
    for item in file_items:
        file_name, file_extn = item.split('.')
        decrypt(filepath,file_name, file_extn, os.getenv("key"))
        print("Decrypted")
    subprocess.Popen(os.getenv('Encrypted_files_path')) 
    while True:
        if keyboard.is_pressed('e'):
            break

    key=generatekey()
    set_key(".env","key",key.decode("utf-8"))
    print(key)
    for item in file_items:
        file_name, file_extn = item.split('.')
        encrypt(filepath,file_name, file_extn, key)
        print('Encrypted')
    



