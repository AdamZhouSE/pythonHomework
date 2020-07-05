s=input().split(" ")
n=int(s[0])
t=int(s[1])
num=input().split(" ")
for i in range(n):
    num[i]=int(num[i])
num.sort()
count=0
for j in range(n):
    if t<=num[j]:
        break
    t=t-num[j]
    count+=1
    if count==n:
        break
print(count)