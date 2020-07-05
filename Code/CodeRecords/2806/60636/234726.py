num=int(input(""))
list=[]
for i in range(num):
    list.append(input(""))
price=[]
amount=[]
for i in range(num):
    amount.append(int(list[i].split(" ")[0]))
    price.append(int(list[i].split(" ")[1]))
sum=0
while(len(price)!=1):
    a=0
    for i in range(len(price)):
        if(price[i]==min(price)):
            a=i
            break
    for i in range(a,len(price)):
        sum=sum+price[a]*amount[i]
    if(a!=0):
        price=price[:a]
    else:
        break
if(a==1):
    sum=sum+price[0]*amount[0]
print(sum)
