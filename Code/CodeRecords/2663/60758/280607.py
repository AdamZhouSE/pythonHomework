n=int(input())
l=[]
base=3
current=7
while base<100000:
    l.append(base)
    base+=current
    current+=4
for i in range(0,n):
    x=int(input())
    print(l[x-1])