cases=int(input())
for i in range(cases):
    str=input()
    maxlen,tmplen=-1,-1
    for i in range(len(str)-1):
        for j in range(i+1,len(str)):
            if str[j]==str[i]:
                tmplen=j-i-1
                if tmplen>maxlen:maxlen=tmplen
    if str[-2]==str[-1]:tmplen=0
    if tmplen>maxlen:maxlen=tmplen
    print(maxlen)