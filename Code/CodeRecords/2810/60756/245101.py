n=list(map(int,list(input())))
L=len(n)
strList=[]
while n.count(0)!=L:
    str=[]
    for i in range(L):
        if n[i]>=1:
            n[i]-=1
            str.append('1')
        else:
            if '1' in str:
                str.append('0')
    strList.append(''.join(str))
print(len(strList))
print(' '.join(strList))