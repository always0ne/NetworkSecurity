# Created by always0ne on 2020.09.16

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def decrypt_message_rsa():
	passphrase = input("passphrase : ")
	# get key pair from private key
	with open("private.pem",'rb') as private_key:
		key_pair = RSA.import_key(private_key.read(),passphrase=passphrase)
		
	# decrypt message and print
	decryptor = PKCS1_OAEP.new(key_pair)
	with open("enc.txt",'rb') as encrypted_message:
		print(decryptor.decrypt(encrypted_message.read()))

decrypt_message_rsa()
