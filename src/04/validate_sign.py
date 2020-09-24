# Created by always0ne on 2020.09.24

from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_PSS
from Crypto.Hash import SHA

def validate_sign():
	# get key pair from private key
	with open("public.der",'rb') as public_key:
		pub_key = RSA.import_key(public_key.read())	
		# decrypt message and print
		with open("1.txt",'rb') as message:
			h = SHA.new()
			h.update(message.read())
			verifier = PKCS1_PSS.new(pub_key)
			with open("sig.txt", 'rb') as sign:
				if verifier.verify(h,sign.read()):
					print("verified")
				else:
					print("not verified")

validate_sign()
