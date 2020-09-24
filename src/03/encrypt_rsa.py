# Created by always0ne on 2020.09.16

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def encrypt_message_rsa():
	message = input("input your message : ")
	# generate RSA Key
	key_pair = RSA.generate(3072)
	pub_key = key_pair.publickey()
	
	# generate Private Key and save private.pem
	with open("private.pem",'wb') as private_key:
		private_key.write(key_pair.export_key(passphrase="1234"))
	
	# encrypt message and save enc.txt
	encryptor = PKCS1_OAEP.new(pub_key)
	with open("enc.txt",'wb') as encrypted_message:
		encrypted_message.write(encryptor.encrypt(message.encode('utf-8')))

encrypt_message_rsa()
