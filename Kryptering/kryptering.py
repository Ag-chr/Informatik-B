from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii
import random

# opgaver: https://aarhustech.itslearning.com/ContentArea/ContentArea.aspx?LocationID=47784&LocationType=1

# greatest_common_divisor
def gcd(a, b):
    while True:
        if a == 0:
            return b
        temp = a
        a = b % a
        b = temp

def euler_totient(n):
    result = 1
    for i in range(2, n):
        if gcd(i, n) == 1:
            result += 1
    return result


class Person:
    def __init__(self):
        self.keyPair = RSA.generate(1024)
        self.p = self.keyPair.p
        self.q = self.keyPair.q
        self.n = self.p * self.q

        self.euler = euler_totient(self.n)
        self.e = random.randint(2, self.euler - 1)
        while gcd(self.e, self.euler) != 1:
            self.e = random.randint(2, self.euler - 1)


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