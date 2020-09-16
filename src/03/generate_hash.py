# Create by always0ne on 2020.09.16

from Crypto.Hash import HMAC

def generate_hash(filename):
	password = input("Key : ")
	h = HMAC.new(password.encode('utf-8'))
	with open(filename, 'rb') as message:
		h.update(message.read())
		print(h.digest())
		with open("H.txt",'wb') as hash_value:
			hash_value.write(h.digest())
	
generate_hash('1.txt')
