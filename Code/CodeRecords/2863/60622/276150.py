l=input().split()
n=int(l[0])
h=int(l[1])
l=list(map(int,input().split()))
count=0
for i in range(n):
    if l[i]>h:
        count+=2
    else:
        count+=1
print(count)