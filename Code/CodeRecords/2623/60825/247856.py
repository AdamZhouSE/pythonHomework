aaa=input()
l=aaa.split(",")
l= list(map(int, l))

k=int(input())

l.sort()
last=l[0]-1
i=0
for x in l:
    if x>last:
        i+=1
    if i==k:
        print(x)
        break
    last=x