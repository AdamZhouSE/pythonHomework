n=int(input())
l=list(map(int,input().split()))
l.sort()
wait=0
Sum=0
for i in l:
    if i>=wait:
        wait+=i
        Sum+=1
print(Sum)