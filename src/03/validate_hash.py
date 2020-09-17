# Create by always0ne on 2020.09.16

from Crypto.Hash import HMAC

def check_hash(filename):
	password = input("Key : ")
	h = HMAC.new(password.encode('utf-8'))
	with open('H.txt', 'rb') as message:
		h.update(message.read(os.path.getsize("H.txt")-16))
		print(h.digest())
		if h.digest() == message.read():
			print("OK")
		else:
			print("NOK")
	
check_hash('1.txt')
