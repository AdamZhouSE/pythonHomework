n=int(input())
num_list=list(map(int,input().split(" ")))
amount=0
num_list.sort()
amount1=0
amount2=0
for i in range(int(n/2)):
    amount1+=num_list[i]
for j in range(int(n/2),n):
    amount2+=num_list[j]
amount=amount1*amount1+amount2*amount2
print(amount)