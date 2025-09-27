keys = generate_key(100)

msg = "A"*1000000
msg = int_encode_str(msg)
dados = encrypt(msg,keys['pub'])
print(dados)
dec = decrypt(dados,keys['priv'])
print(dec)
print(int_decode_str(dec))