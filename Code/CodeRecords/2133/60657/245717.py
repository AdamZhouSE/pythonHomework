n=input().split(',')
n=[int(i) for i in n]
con=0
n.sort()
num=n.count(n[-1])
cons=0
while num!=len(n):
    for i in range(len(n)-1):
        n[i]+=1
    cons += 1
    n.sort()
    num = n.count(n[-1])
print(cons)