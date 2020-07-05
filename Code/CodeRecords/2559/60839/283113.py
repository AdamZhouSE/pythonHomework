def isIosgram(s):
    st=list(s)
    for i in range(0,len(st)-1):
        for j in range(i,len(st)-1):
            if st[i]==st[j+1]:
                return 0
    return 1

n=int(input())
s=[]
for i in range(0,n):
    s.append(isIosgram(input()))

for i in range(0,n):
    print(s[i])