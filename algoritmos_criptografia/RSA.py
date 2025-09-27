from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

class RivestShamirAdleman:
    def __init__(self,size_key=2048):
        self.__chave_privada = RSA.generate(size_key)
        self.__chave_publica = self.__chave_privada.public_key()
        self.__key = size_key;
        print(self.__chave_privada)
        print(self.__chave_publica)

    def encriptar(self,mensagem):
        cifra = PKCS1_OAEP.new(self.__chave_publica)
        str_encrypted = "".encode('utf-8')
        for i in range(0,len(mensagem),self.__key//8 - 48):
            chunk = mensagem[i:i + self.__key//8 - 48]
            str_encrypted += cifra.encrypt(chunk.encode('utf-8'))
        return str_encrypted
    
    def decriptar(self,mensagem):
        decript = PKCS1_OAEP.new(self.__chave_privada)
        str_decript = b''
        for i in range(0,len(mensagem),self.__key//8):
            chunk = mensagem[i:i + self.__key//8]
            str_decript += decript.decrypt(chunk)
            
        return str_decript.decode('utf-8')