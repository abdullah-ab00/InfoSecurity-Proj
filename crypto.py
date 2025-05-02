from kyber_py.kyber.default_parameters import Kyber512
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os


# Pre-configured Kyber512 instance
kyber = Kyber512

def generate_keys():
    """
    Generates a Kyber512 key pair.
    Returns:
        tuple(bytes, bytes): (public_key, private_key)
    """
    public_key, private_key = kyber.keygen()
    return public_key, private_key



# Inside encrypt_message():
def encrypt_message(public_key_hex, message):
    public_key = bytes.fromhex(public_key_hex)
    shared_secret, ciphertext = kyber.encaps(public_key)
    
    cipher_aes = AES.new(shared_secret, AES.MODE_CBC)
    ct_bytes = cipher_aes.encrypt(pad(message.encode(), AES.block_size))
    iv = cipher_aes.iv

    return ciphertext + iv + ct_bytes, None


# Inside decrypt_message():
def decrypt_message(private_key_hex, ciphertext_hex):
    private_key = bytes.fromhex(private_key_hex)
    ciphertext = bytes.fromhex(ciphertext_hex)

    KYBER_CIPHERTEXT_BYTES = 768  # ✅ correct length for Kyber512
    kyber_ct = ciphertext[:KYBER_CIPHERTEXT_BYTES]
    aes_ct = ciphertext[KYBER_CIPHERTEXT_BYTES:]

    shared_secret = kyber.decaps(private_key, kyber_ct)

    iv = aes_ct[:16]
    ct = aes_ct[16:]

    cipher = AES.new(shared_secret, AES.MODE_CBC, iv=iv)
    decrypted = unpad(cipher.decrypt(ct), AES.block_size)

    return decrypted.decode('utf-8')


