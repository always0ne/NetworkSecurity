# Created by always0ne on 2020.09.08

# AES pycrypto package
from Crypto.Cipher import AES

# key has to be 16, 24 or 32 bytes long
secretKey = 'secret-key-im-always0ne!'

while(1):
	message = input("Input your message : ")
	# Encrypt AES with CFB mode
	encrypt_AES = AES.new(secretKey, AES.MODE_CFB, 'This is an IV-12')
	ciphertext = encrypt_AES.encrypt(message)
	print("Cipher text: " , ciphertext)
	
	# Decrypt AES with CFB mode
	decrypt_AES = AES.new(secretKey, AES.MODE_CFB, 'This is an IV-12')
	message_decrypted =  decrypt_AES.decrypt(ciphertext)
	print("Decrypted text: ",  message_decrypted.strip())
