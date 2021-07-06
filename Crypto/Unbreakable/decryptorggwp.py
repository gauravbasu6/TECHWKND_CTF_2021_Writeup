test="This is a test message. In cryptography, the one-time pad (OTP) is an encryption technique that cannot be cracked, but requires the use of a single use pre-shared key that is no smaller than the message being sent."
out='''|v9zXv4jsV"w	j
J)$RPb3JrDHkx,4/x7 AGv'''

key=''
for i in range(len(out)):
    key+=chr(ord(test[i])^ord(out[i]))

c='''|[A/=KPpcLt<f%	FL
=gF}^yd'''
flag=''
for i in range(len(c)):
    flag+=chr(ord(c[i])^ord(key[i]))
print(flag)
