from cryptography.fernet import Fernet
from dotenv import load_dotenv
from dotenv import set_key
import os
import keyboard

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

def decrypt(filepath,filename, fileextn, key):
    cipher_suite = Fernet(key)
    with open(filepath + "/" + filename + "." + fileextn, "rb") as file:
        data=file.read()
        file.close
    decrypted_data=cipher_suite.decrypt(data)
    with open(filepath + "/" + filename + "." + fileextn, "wb") as file:
        file.write(decrypted_data)

    # with open("D:\FiletoProtect\IMG_20210516_105253_764.jpg",'rb') as file:
    #     plain = file.read()
    # encrypted_data=cipher_suite.encrypt(plain)
    # with open("D:\FiletoProtect\IMG_20210516_105253_764.jpg",'wb') as file:
    #     file.write(encrypted_data)
    #     file.close()
        
def encrdecr():
    key=generatekey()
    filepath = os.getenv('encrypted_files')
    file_items = os.listdir(filepath)

    for item in file_items:
        file_name, file_extn = item.split('.')
        encrypt(filepath,file_name, file_extn, key)
    while True:
        if keyboard.is_pressed('d'):
            break
    for item in file_items:
        file_name, file_extn = item.split('.')
        decrypt(filepath,file_name, file_extn, key)



