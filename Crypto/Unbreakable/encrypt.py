from random import randint

test= "This is a test message. In cryptography, the one-time pad (OTP) is an encryption technique that cannot be cracked, but requires the use of a single use pre-shared key that is no smaller than the message being sent."

f= open('flag.txt','r')
flag= f.readline()
f.close()

o= open('out.txt','w',encoding="utf-8")

def xor(m,k):
    k= k[:len(m)]
    c= ''
    for a,b in zip(m,k):
        c= c + chr(ord(a)^ord(b))
    return c

def keygen(l):
    key= ''
    for i in range (1,l):
        key= key + chr(randint(0,128))
    return key

key= keygen(len(test))

test_cipher= xor(test,key)
cipher= xor(flag,key)

o.write(test_cipher)
o.write("\n***********************************\n")
o.write(cipher)

