arr=[]
m,n=0,0
for i in range(5):
    l=input().split()
    for j in range(5):
        if l[j]=='1':
            m=i
            n=j
            break
print(abs(m-2)+abs(n-2))

