num = int(input())
need = []
price = []
for i in range(num):
    a,b = map(int, input().split())
    price.append(b)
    need.append(a)
#print(num)
adder = 1
index = num
while True:
#    print(True)
    request = 0
    mins = min(price)
    for i in price:
        if i==mins:
            index=i
            break
    length = len(price)
    for i in range(index,length):
        request +=need[i]
        price.pop()
    if len(price)==0:
        break
    adder+=(request*mins)
print(adder)