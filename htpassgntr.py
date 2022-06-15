#!/usr/bin/env python3
import hashlib

user=input("username: ")
sandi=input("password: ")

htpass= hashlib.sha1(sandi.encode())

password = htpass.hexdigest()
#concate username with hash password
htpassword = user + ":" + password
print(htpassword) 
print("Jika anda lupa, cari file passgen.txt\n")
#open file and write the hash result
f=open("passgen.txt","w+")
f.write(htpassword)
f.close()
