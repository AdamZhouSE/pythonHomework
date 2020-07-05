num=int(input())
sum=0
s=input().split(' ')
s=list(map(int,s))
max=s[0]
for i in range(num):
    if(s[i])>max:
        max=s[i]
    sum=sum+s[i]
print(max*num-sum)