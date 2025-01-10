from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii

# opgaver: https://aarhustech.itslearning.com/ContentArea/ContentArea.aspx?LocationID=47784&LocationType=1

class Person:
    def __init__(self):
        self.keyPair = RSA.generate(1024)
        self.pubKey = self.keyPair.public_key()

    def print_public_key(self):
        pubKeyPEM = self.pubKey.exportKey()
        print(pubKeyPEM.decode('ascii'))

    def print_encrypted_message(self, encrypted):
        print("Encrypted:", binascii.hexlify(encrypted))

    def encrypt_message(self, msg, pubKey):
        encryptor = PKCS1_OAEP.new(pubKey)
        encrypted = encryptor.encrypt(msg.encode("utf-8"))
        return encrypted

    def decrypt_message(self, encrypted):
        decryptor = PKCS1_OAEP.new(self.keyPair)
        decrypted = decryptor.decrypt(encrypted)
        return decrypted



# Opgave A
alice = Person()
bob = Person()
print("HEJ".encode("utf-8"))

# 1: Alice krypterer en besked med Bobs offentlige nøgle,
# og sender den resulterende cipher til Bob,
# som dekrypterer den med sin hemmelige nøgle.
alice_encrypteret_besked = alice.encrypt_message("Hej bob du er the GOAT", bob.pubKey)
alice.print_encrypted_message(alice_encrypteret_besked)

print("bobs dekrypterede besked:")
print(bob.decrypt_message(alice_encrypteret_besked))


