tmp=input().split()
n=int(tmp[0])
m=int(tmp[1])
li=list(map(int,input().split()))
for i in range(m):
    tmp=input().split()
    op=(int(tmp[0]))
    l=(int(tmp[1]))-1
    r=(int(tmp[2]))-1
    if op==0:
        li=li[0:l]+sorted(li[l:r+1])+li[r+1:]
    else:
        li=li[0:l]+sorted(li[l:r+1])[::-1]+li[r+1:]
q=int(input())-1
print(li[q])
