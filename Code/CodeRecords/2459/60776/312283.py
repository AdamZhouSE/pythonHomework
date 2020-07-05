a=input().split(' ')
yanshi=int(a[1])
result=0
b=input().split(' ')
chufa=[]
for i in range(0,len(b)):
    b[i]=int(b[i])
for i in range(0,len(b)):
    chufa.append(0)
for i in range(yanshi+1,yanshi+len(b)+1):
    max=0
    for j in range(0,min(i,len(b))):
        if b[j]>=b[max]:
            max=j
    result+=b[max]*(i-max-1)
    chufa[max]=i
    b[max]=0
print(result)
print(" ".join(str(i) for i in chufa))