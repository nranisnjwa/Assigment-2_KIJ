from cryptography.fernet import Fernet

#Generating a random key
key = Fernet.generate_key()
#Creating the symmetric random key
cipher = Fernet(key)

#create the cipher
cipher = Fernet(key)

with open('symmetric_key','wb') as k:
    skey = k.write(key)

#open file for encrypt
myfile = open('try.pdf','rb')
myfiledata= myfile.read()

#encrypt the data
encrypted_data = cipher.encrypt(myfiledata)
edata = open('encrypted_file','wb')
edata.write(encrypted_data)
