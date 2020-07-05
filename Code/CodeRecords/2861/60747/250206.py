n= int(input())
count=0
num = input().split(" ")
for i in range(n):
    num[i]=int(num[i])
num.sort()
j=n
while j >0:
    count=num[j-1]-num[j-2]+count
    j-=2
print(count)