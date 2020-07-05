a=int(input())
b=input().split()
smith=0
rank=1
for i in range(4):
    b[i]=int(b[i])
    smith=smith+b[i]
for j in range(a-1):
    c=input().split()
    score=0
    for k in range(4):
        c[k]=int(c[k])
        score=score+c[k]
    if score>smith:
        rank+=1
print(rank)     