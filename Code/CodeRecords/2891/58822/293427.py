num=int(input())
sum=0
s=input().split(' ')
s=list(map(int,s))
for i in range(num):
    sum=sum+s[i]
print(sum)