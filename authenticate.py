import tkinter as tk
import os,sys
import EncryptDecrypt
import FaceRecognition
import cv2
from dotenv import load_dotenv
from tkinter import messagebox

load_dotenv()

def open_folder():
    fr = FaceRecognition.FaceRecognize()
    name = fr.run_recognition()
    owner = os.getenv('Authorised_User')
    if name is not None:
        print(name)
        print(owner)
        if name == owner:
            cv2.destroyAllWindows()
            EncryptDecrypt.encrdecr()

        else:
            root = tk.Tk()
            root.withdraw()
            messagebox.showerror("Error", "Unknown Person.")
            sys.exit()

if __name__ == "__main__":
    open_folder()

