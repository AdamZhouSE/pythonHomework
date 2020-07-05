s=input().split(" ")
num=[]
max_T=int(s[1])
for i in range(int(s[0])):
    num.append(int(input()))
num.sort()
sum=0
for j in range(len(num)):
    sum=sum+num[j]
t=int(sum/max_T)+1
if t<len(num)/2:
    print(t+1)
else:
    print(int(sum/max_T)+1)
