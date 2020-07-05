n=int(input())
num_list=[]
amount_list=[]
price_list=[]
min_price=100
amount=0
for  i in range(n):
    temp_list=list(map(int,input().split(" ")))
    num_list.append(temp_list)

for j in range(n):
    amount_list.append(num_list[j][0])
    price_list.append(num_list[j][1])

for k in range(n):
    if price_list[k]<=min_price:
        min_price=price_list[k]
        amount+=price_list[k]*amount_list[k]
    else:
        amount+=amount_list[k]*min_price
print(amount)
    