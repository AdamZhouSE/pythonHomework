n=int(input())
st=[[0 for i in range(256)] for i in range(20)]
for i in range(n):
    st[i]=str(input())
    minStr,minLen=256,256
    if len(st[i])<minLen:
        minLen=len(st[i])
        minStr=i
max=0
for i in range(minLen):
    for j in range(minLen-i):
        dest=st[minStr][i:j]
        ok=1
        for k in range(n):
            if dest not in st[k]:
                ok=0
                break
        if ok==1 and len(dest)>max:
            max=len(dest)
            ans=dest
print(len(ans))