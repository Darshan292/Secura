
# Secura: Enhanced Face Recognition and Anti-Spoofing System

## Overview
Secura employs real-time facial recognition for user authentication, granting access to files. Strong encryption ensures data security, automatically decrypting for authorized users and re-encrypting when closed. The system now includes an advanced anti-spoofing mechanism to ensure that only real faces are authenticated.

## Features

### 🔒 Advanced Security
Anti-Spoofing Technology: Leverage state-of-the-art YOLO model to differentiate between real and fake faces, ensuring that only genuine users are authenticated.

Real-Time Facial Recognition: Instantly identify and authenticate users using a robust facial recognition system powered by the face_recognition library.

Dynamic Encryption: Automatically encrypt and decrypt sensitive files based on user authentication, providing seamless and secure access.
### ⚡ High Performance
Efficient Processing: Optimized algorithms for real-time face detection and recognition, ensuring minimal latency.

Adaptive Encryption Keys: Generate new encryption keys on-the-fly for every session, enhancing security without compromising performance.
### 🛠️ Easy Integration and Use
User-Friendly Interface: Simple and intuitive GUI built with Tkinter for effortless interaction and operation.

Environment Configuration: Easily configurable settings through a .env file, allowing quick setup and deployment.

Cross-Platform Compatibility: Designed to work on multiple platforms, including Windows, macOS, and Linux.
### 📂 Comprehensive File Management
Automatic Encryption/Decryption: Securely encrypt files when added to the sensitive folder and decrypt them when accessed by authorized users.

Key Management: Flexible key management system that supports both dynamic and static key usage, ensuring optimal security practices.

## Encryption Method
Secura uses the Fernet encryption and decryption scheme from the cryptography library. Fernet is a symmetric-key encryption algorithm that uses the Advanced Encryption Standard (AES) algorithm in Cipher Block Chaining (CBC) mode with a 128-bit key for encryption.

A new key is produced every time the files are re-encrypted. If you want to use a single key, you can skip the key generation part while re-encrypting. You can save the key either as a separate file or as a value for a variable in the .env file.

## How to Use Secura
1. Specify the Path:

- Specify the path of the authorized user's image as People_images_path.
- Save the path of the sensitive folder as encrypted_files in the .env file.
2. Run the Program:

- Run the authenticate.py script to start the authentication process.
- The sensitive folder will be opened. Add the files that need to be encrypted into the folder.
- Press the specified key to encrypt the files and stop the program.
3. Subsequent Runs:

- The sensitive folder will be opened for the authorized user, and the files will be decrypted.

## Project Structure
- antispoof.py: Contains the anti-spoofing logic using the YOLO model to classify faces as real or fake.
- EncryptDecrypt.py: Handles the encryption and decryption of files using the cryptography library.
- Facerecognition.py: Performs face recognition using the face_recognition library and the YOLO model for real/fake detection.
- authenticate.py: Main script that integrates face recognition, anti-spoofing, and file encryption/decryption for user authentication.
- .env: Environment file to store sensitive information such as the encryption key and paths.

## Prerequisites
- Python 3.6+
- Pip (Python package installer)
### Python libraries:
- opencv-python
- cvzone
- face_recognition
- cryptography
- ultralytics (for YOLO model)
