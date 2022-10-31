import rsa

#create the pub & private keys
(pubkey, privkey) = rsa.newkeys(2048)

#write the public key to a file
with open('publickey.key', 'wb') as key_file:
    key_file.write(pubkey.save_pkcs1('PEM'))
    print("Public Key was created")

#write the private key to a file
with open('privatekey.key', 'wb') as key_file:
    key_file.write(privkey.save_pkcs1('PEM'))
    print("Private Key was created")
