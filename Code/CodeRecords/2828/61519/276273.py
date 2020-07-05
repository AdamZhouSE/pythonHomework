n=int(input())
power=0
num=list(input().split(" "))
for i in range(n):
    num[i]=int(num[i])
money=num[0]
for i in range(1,n-1):
    if num[i]>=num[i+1]:
        power=power+num[i]-num[i+1]
    else:
        if power>=(num[i+1]-num[i]):
            power=power-(num[i+1]-num[i])
        else:
            x=(num[i+1]-num[i])-power
            power=0
            money=money+x
print(money)