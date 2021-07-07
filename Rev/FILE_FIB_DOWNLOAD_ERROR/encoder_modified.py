# while getting some secret codes, we found an encoder program. However, during the download of the encoder code,
# we lost CONNEC..................#^*$#&^$^*#@$^*&#@^$*&^*$#*&^ thereby corruptin$&*#$&#() file
# the flag is of *&$##$($#_)(@$)_(#_)$ importance


# all we know is the output of this code
# TFDJZPVQ{SÃŁǘʖПځ੉Ⴉ᪞⫲䕽灐땑𒕆𝪐𯾅񍦣񽣥󋉴}
# it seems encoded. use your smarts to figure out how to decode it

flag = 'TFDJZPVQ{SÃŁǘʖПځ੉Ⴉ᪞⫲䕽灐땑𒕆𝪐𯾅񍦣񽣥󋉴}'

x = len(flag)

def somefunc(i):
    a = 0
    b = 1
    if i == 0:
        return 0

    if i == 1:
        return 1

    if i >= 2:
        c = 0
        for ctr in range(1,i):
            c = a + b
            a = b
            b = c

        return c


for i in range(0, x):
    if flag[i] == '{' or flag[i] == '}':
        print(flag[i], end='')
    else:
        print(chr(ord(flag[i])-somefunc(i)), end='')

