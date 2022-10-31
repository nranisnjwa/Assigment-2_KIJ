import rsa


#Open key file and return key data
def file_open(file):
    key_file = open(file, 'rb')
    key_data = key_file.read()
    key_file.close()
    return key_data


#Open private key file
privkey = rsa.PrivateKey.load_pkcs1(file_open('privatekey.key'))


myfile = file_open('try.pdf')
hash_value = rsa.compute_hash(myfile, 'SHA-512')  



#Sign the message with the sender private key
signature = rsa.sign(myfile, privkey, 'SHA-512')

s = open('signature_file','wb')
s.write(signature)


print(signature)
print(len(signature))

print(len(hash_value) * 8) 

