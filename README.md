# Secura

Secura employs real-time facial recognition for user authentication, granting access to files. Strong encryption ensures data security, automatically decrypting for authorized users and re-encrypting when closed.

## Encryption Method
 Secura uses Fernet encryption and decryption scheme from the cryptography library. Fernet is a symmetric-key encryption algorithm that uses the Advanced Encryption Standard (AES) algorithm in Cipher Block Chaining (CBC) mode with a 128-bit key for encryption.

 A new key is produced every time when the files are re-encrypted, if you want to use single key then you can skip the key generating part while re-encrypting.
You can save the key either as a separate file or as a value for a variable in .env file.


## How to use Secura
1. To encrypt the files initially, add the sensitive file to a folder and then execute the encryption function.
2. Save the path of the folder as "encrypted_files" in .env file.
3. Save the folder path which contains authorised user's image as "People_images_path".
4. For encryption you can also use Vernam Cipher algorithm which uses xor operation for encryption and decryption (as in Encrypt_Decrypt.py)
