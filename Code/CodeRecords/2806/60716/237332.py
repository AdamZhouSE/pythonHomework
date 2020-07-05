num = int(input())
price = []
need = []
for i in range(num):
    a,b = map(int, input().split())
    price.append(b)
    need.append(a)
adder = 0
index = num
while index<1:
    request = 0
    mins = min(price)
    for i in price:
        if i==mins:
            index=i
            break
    for i in range(index,num):
        request +=need[i]
        price.pop(i)
    adder+=(request*mins)
print(adder)