n=int(input())
lis=list(map(int,input().split(" ")))

even=0
odd=0
e=[]
o=[]
for i in lis:
    if i%2==0:
        even+=1
        e.append(i)
    else:
        odd+=1
        o.append(i)
od=set(o)
ev=set(e)
m=0
for i in od:
    for j in ev:
        if m<abs(i-j):
            m=abs(i-j)
smaller=odd if odd<even else even
print(smaller)