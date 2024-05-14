from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

# generates the public and private keys, the pub key is found in the object in which holds the creation of priv key

private_key = rsa.generate_private_key(
 public_exponent=65537,
 key_size = 2048,
 backend= default_backend()
)
public_key = private_key.public_key()

# serialize the private key and store it to a file
pem = private_key.private_bytes(
 encoding= serialization.Encoding.PEM,
 format = serialization.PrivateFormat.PKCS8,
 encryption_algorithm= serialization.NoEncryption()
)
with open('private.key', 'wb') as private_file:
 private_file.write(pem)

# serialize the public key and store it to a file
pem = public_key.public_bytes(
 encoding= serialization.Encoding.PEM,
 format = serialization.PublicFormat.SubjectPublicKeyInfo
)

with open('public.key', 'wb') as public_file:
 public_file.write(pem)
