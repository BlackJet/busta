# -*- coding: utf-8-*-
from Crypto.Cipher import AES
from Crypto.Hash import MD5,SHA256
import base64

def encrypt_text(key,text):
    hash = SHA256.new(key).hexdigest()
    crypter = AES.new(hash[:32],AES.MODE_CFB,IV = bytes(hash[:16]))
    return base64.b64encode(crypter.encrypt(text.encode('utf-8'))).decode()

def decrypt_text(key,text):
    hash = SHA256.new(key).hexdigest()
    decrypter = AES.new(hash[:32],AES.MODE_CFB,IV = bytes(hash[:16]))
    return decrypter.decrypt(base64.b64decode(text.encode())).decode('utf-8')

def hash_text(text):
    return MD5.new(text).hexdigest()