f=input().split()
num=int(f[0])
h=int(f[1])
people=input().split()
people=sorted(list(map(int,people)))
count=0
for x in people:
    if x>h:
        count+=1
print((num-count)+count*2)