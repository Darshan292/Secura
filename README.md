# Secura

Secura employs real-time facial recognition for user authentication, granting access to files. Strong encryption ensures data security, automatically decrypting for authorized users and re-encrypting when closed.

## Encryption Method
 Secura uses Fernet encryption and decryption scheme from the cryptography library. Fernet is a symmetric-key encryption algorithm that uses the Advanced Encryption Standard (AES) algorithm in Cipher Block Chaining (CBC) mode with a 128-bit key for encryption.

 A new key is produced every time when the files are re-encrypted, if you want to use single key then you can skip the key generating part while re-encrypting.
You can save the key either as a separate file or as a value for a variable in .env file.


## How to use Secura
1. Specify the path of authorised user's image as "People_images_path".
2. Save the path of the sensitive folder as "encrypted_files" in .env file.
3. Run the program, the sensitive folder will be opened. Add the files that has to be encrypted into the folder.
4. Press the specified key inorder to encrypt the files and stop the program.
5. Next time when you run the program the sensitive folder will be opened for authorised user and the files will be decrypted.
