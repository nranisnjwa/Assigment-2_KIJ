import rsa


#Open key file and return key data
def file_open(file):
    key_file = open(file, 'rb')
    key_data = key_file.read()
    key_file.close()
    return key_data


#Open private key file
privkey = rsa.PrivateKey.load_pkcs1(file_open('privatekey.key'))

#Open the file and return data to variable
myfile = file_open('symmetric_key','wb')
hash_value = rsa.compute_hash(myfile, 'SHA-512') 

#Sign the pdf with the sender private key
signature = rsa.sign(myfile, privkey, 'SHA-256')

