n=int(input())
fail=0
li=[0 for i in range(100)]
for i in range(n):
    a,b=input().split(' ')
    if a=='T':
        fail+=1
        li[fail]=b
    if a=='U':
        fail-=int(b)
    if a=='Q':
        print(li[int(b)])