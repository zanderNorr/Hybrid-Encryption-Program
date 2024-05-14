from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

# reciever will transmit the encrypted shared key to sender, then sender will transmit the decrypted shared key to the reciever

def main():
    with open('private.key', 'rb') as file:
        private_key_unserialized = file.read()

    private_key = serialization.load_pem_private_key(
        private_key_unserialized, password=None, backend=default_backend()
    )
    with open("EncryptedSharedKey", "rb") as file:
        shared_key_encrypted = file.read()
    shared_key_decrypted = private_key.decrypt(
        shared_key_encrypted,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None,
        ),
    )
    return shared_key_decrypted

if __name__ == '__main__':
    with open('DecryptedSharedKey', 'wb') as file:
        key = main()
        file.write(key)