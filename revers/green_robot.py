#OLD
from base64 import *
from Crypto.Cipher import AES

#флаг находился в директории com в JADX
secretKey = "23ffabcde582ffacb49323fcbaddefac"
iv = "89438fabcd849298"
correctEncryptedString = "d5RIYRoC/3bQyfM8TSOlo463lgAMeSkAi/s8CEn1pMw="

key = secretKey.encode()
iv = iv.encode()
ct = b64decode(correctEncryptedString)

task = AES.new(key, AES.MODE_CBC, iv=iv).decrypt(ct)
l = task[-1]
ans = task[:-l].decode()
print(ans)
