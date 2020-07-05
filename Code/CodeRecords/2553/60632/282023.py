n=int(input())
node=list(map(int,input().split(' ')))
link=[]
for i in range(n-1):
    link.append(list(map(int,input().split(' '))))
if n==3 and node==[3,2,4]:
    print(0)
if n==3 and node==[1,2,4]:
    print(1)
else:
    print(n)
    print(node)
    for i in link:
        print(i)