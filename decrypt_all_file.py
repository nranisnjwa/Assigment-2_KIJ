import rsa

#Open key file and return key data
def file_open(file):
    key_file = open(file, 'rb')
    key_data = key_file.read()
    key_file.close()
    return key_data


#Open public key file
pubkey = rsa.PublicKey.load_pkcs1(file_open('publickey.key'))

pdf = file_open('try.pdf')
signature = file_open('signature_file')

#Verify the signature to show if successful or failed
try:
    rsa.verify(pdf,signature,pubkey)
    print("Signature successfully verified")

except:
    print("Warning!!!! Signature could not be verified")
