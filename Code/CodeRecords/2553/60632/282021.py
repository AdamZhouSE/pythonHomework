n=int(input())
node=list(map(int,input().split(' ')))
link=[]
for i in range(n-1):
    link.append(list(map(int,input().split(' '))))
print(n)
print(node)
for i in link:
    print(i)