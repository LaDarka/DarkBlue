

import hashlib 

class Cipher_Connection:
	def Hashed_File(self, messegeEncrypt):
		file_Encrypt = hashlib.sha256(messegeEncrypt.encode("UTF"))
		New_EncryptFile = file_Encrypt.hexdigest()
		return New_EncryptFile
