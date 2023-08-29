import tkinter as tk
import os,sys
import Encrypt_Decrypt
import FaceRecognition
import pygetwindow as gw
import subprocess, time
import cv2
import keyboard
from dotenv import load_dotenv

load_dotenv()

def check_password(people, owner):
    # Compare the entered password with the correct password
    if owner in people:
        if float(people[owner]) > 95.00:
            return True
        

def open_folder():
    fr = FaceRecognition.FaceRecognize()
    name_list = fr.run_recognition()
    name=[]
    owner = os.getenv('Authorised_User')
    people = {}
    for items in name_list:
        start_index = items.find("(")
        end_index = items.find("%")
        name.append(items.split()[0])
        people[items.split()[0]]=items[start_index+1:end_index]
    if name is not None:
        print(name)
        print(people)
        if check_password(people, owner):
            cv2.destroyAllWindows()
            Encrypt_Decrypt.main()
            subprocess.Popen(os.getenv('Encrypted_files_path'))  
            while True:
                if keyboard.is_pressed('c'):
                    break
            Encrypt_Decrypt.main()
        else:
            tk.messagebox.showerror("Error", "Unknown Person.")
            sys.exit()

def main():

    open_folder()


if __name__ == "__main__":
    main()

