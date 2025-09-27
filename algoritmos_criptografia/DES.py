from Crypto.Cipher import DES

class DataEncryptionStandard:
    def __init__(self,chave):
        self.cipher = DES.new(chave.encode('utf-8'), DES.MODE_ECB)

    def __ajustar_frase(self,frase):
        if len(frase.encode("utf-8")) % 8 == 0:
            return frase.encode("utf-8")
        
        frase_temp = frase.encode("utf-8")

        while len(frase_temp) % 8 != 0:
            frase_temp += b' '
        return frase_temp
    
    def encriptar(self,frase):
        frase = self.__ajustar_frase(frase)
        dados = self.cipher.encrypt(frase)
        return dados
    
    def decriptar(self,dados):
        return self.cipher.decrypt(dados).decode('utf-8')