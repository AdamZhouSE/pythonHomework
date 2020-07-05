n=int(input())
for i in range(n):
    N=int(input())
    s=input()
    sl=s.split( )
    temp=[]
    for j in sl:
        temp.append(int(j))
    k=int(input())
    mul=1
    for j in temp:
        mul=mul*j
    print(mul%k)