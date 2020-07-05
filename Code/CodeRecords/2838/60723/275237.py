n=int(input())
temp=input().split()
for i in range(n):
    temp[i]=int(temp[i])
temp.sort()
count=0
for i in range(int(n/2)):
    count=count+int(pow(int(temp[i])+int(temp[n-1-i]),2))
print(count)