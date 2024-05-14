import os
from cryptography.fernet import Fernet

#reciever program, which uses the decrypted shared key after reciving from sender

def reciever_decryption(shared_key):
    fernet = Fernet(shared_key)
    # will only decrypt files which are in the local directory of the decrpytion program
    files = os.listdir()

    
    for filename in files:
        if filename.endswith('encrypted'):
            with open(filename, 'rb') as file:
                encrypted_contents = file.read()
            original_message = fernet.decrypt(encrypted_contents)
            decrypted_filename = filename.replace('.encrypted', '')
            with open(decrypted_filename, 'wb') as file:
                file.write(original_message)
            os.remove(filename)

if __name__ == '__main__':
    with open('DecryptedSharedKey', 'rb') as file:
        key = file.read()
    reciever_decryption(key)