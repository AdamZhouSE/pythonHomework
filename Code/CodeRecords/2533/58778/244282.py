s=input()
s=s[1:len(s)-1]
sl=s.split(',')
re=[]
for i in sl:
    if(int(i)%2==0):
        re.append(i)
for i in sl:
    if(int(i)%2==1):
        re.append(i)
numre=[]
for i in re:
    numre.append(int(i))
print(numre)