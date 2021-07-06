import re
flag=[]
h = open('/Users/gaura/Desktop/song.txt')
c = [ x[:-1] for x in h.readlines() ]
h.close()


for line in c:
    num = re.findall(r"(\s+)",line)
    if num:
        num = int(''.join(num).replace(' ','0').replace('\t','1'),2)
        if num in range(255):
            flag.append(chr(num))

for i in range(len(flag)):
    if i%2==0:
        print(flag[i])