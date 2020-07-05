n=input().split()
num=input().split()
n=[int(x) for x in n]
num=[int(x) for x in num]
count=0

for i in range(1,n[0]):
    while num[i]<=num[i-1]:
        num[i]+=n[1]
        count+=1
print(count)