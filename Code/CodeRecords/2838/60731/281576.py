num=int(input())
data=list(map(int,input().split()))
data.sort()
s=0
for i in range(num//2):
    s+=(data[i]+data[num-i-1])**2
print(s)