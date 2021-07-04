import hashlib

s = input('Enter the string :')
md5 = (hashlib.md5(s.encode('utf-8')).hexdigest())
SHA256=(hashlib.sha256(s.encode('utf-8')).hexdigest())
BLAKE2c=(hashlib.blake2s(s.encode('utf-8')).hexdigest())
print("your md5 code is:{}\n your SHA256 code is:{}\n your BLAKE2c code is:{}".format(md5,SHA256,BLAKE2c))
