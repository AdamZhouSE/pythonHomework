s=input()
Str=[]
for i in range(len(s)):
    Str.append(s[i])
inp=input()
for i in range(2):
        inp=inp.strip('[')
        inp=inp.strip(']')
pairs0=inp.split('],[')
pairs=[[] for i in range(len(pairs0))]
for i in range(len(pairs0)):
        pairs[i].append(int(pairs0[i][0]))
        pairs[i].append(int(pairs0[i][2]))
while 1==1:
    count=0
    for i in range(0,len(pairs)):
        a=Str[pairs[i][0]]
        b=Str[pairs[i][1]]
        if a<=b:
            count=count+1
        else:
            Str[pairs[i][0]]=b
            Str[pairs[i][1]]=a
    if count<len(pairs):
        continue
    else:
        break
result=''
for i in range(len(Str)):
    result=result+Str[i]
print(result)

