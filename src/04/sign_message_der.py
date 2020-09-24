# Created by always0ne on 2020.09.24

from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_PSS
from Crypto.Hash import SHA

def sign_message_der():
	# generate RSA Key
	key_pair = RSA.generate(3072)
	
	# save private/public key on DER
	with open("private.der",'wb') as private_key:
		private_key.write(key_pair.export_key(format = 'DER', pkcs=8, passphrase="1234"))
	with open("public.der",'wb') as private_key:
		private_key.write(key_pair.publickey().export_key(format = 'DER', pkcs=8))
	with open("1.txt", 'rb') as message:
	# sign message and save sig.txt
		h = SHA.new()
		h.update(message.read())
		signer = PKCS1_PSS.new(key_pair)
		with open("sig.txt",'wb') as sign_file:
			sign_file.write(signer.sign(h))

sign_message_der()
