# Create by always0ne on 2020.09.16

from Crypto.Hash import HMAC

def check_hash(filename):
	password = input("Key : ")
	h = HMAC.new(password.encode('utf-8'))
	with open(filename, 'rb') as message:
		h.update(message.read())
		print(h.digest())
		with open("H.txt",'rb') as hash_value:
			if hash_value.read() == h.digest():
				print("OK")
			else:
				print("NOK")
	
check_hash('1.txt')
