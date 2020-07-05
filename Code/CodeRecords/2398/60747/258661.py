s=input().split(" ")
num=[]
max_T=int(s[1])
for i in range(int(s[0])):
    num.append(int(input()))
num.sort()
sum=0
for j in range(len(num)):
    sum=sum+num[j]
print(int(sum/max_T)+1)
