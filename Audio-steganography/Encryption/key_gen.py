from Crypto.PublicKey import RSA

key = RSA.generate(2048)
private_key = key.export_key()
file_out = open("User4_private.pem", "wb")
file_out.write(private_key)

public_key = key.publickey().export_key()
file_out = open("User4_public.pem", "wb")
file_out.write(public_key)