n=int(input())
weight=[]
money=[]
num=0
for i in range(n):
    list1=list(input().split(" "))
    weight.append(int(list1[0]))
    money.append(int(list1[1]))
for i in range(n-1):
    if money[i]<money[i+1]:
        money[i+1]=money[i]
for i in range(n):
    num=weight[i]*money[i]+num
print(num)