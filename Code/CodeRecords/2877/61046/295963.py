num=int(input())
test=input().split()
test=list(map(int,test))
p=[]
n=[]
for x in test:
    if x>0:
        p.append(x)
    else:
        n.append(x)
print(sum(p)-sum(n))