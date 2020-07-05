n = int(input())
l=list(map(int,input().split()))
l.sort()
num_s=0
wait_time=0
for i in l:
    if i>=wait_time:
        num_s+=1
        wait_time+=i
print(num_s)