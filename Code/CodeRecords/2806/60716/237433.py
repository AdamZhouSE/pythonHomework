num = int(input())
need = []
price = []
for i in range(num):
    a,b = map(int, input().split())
    price.append(b)
    need.append(a)
#print(num)
adder = 0
index = num
while True:
#    print(True)
    request = 0
    mins = min(price)
    for i in range(len(price)):
        if price[i]==mins:
            index=i
            break
    length = len(price)
    for i in range(index,length):
        request +=need[i]
        price.pop()
    adder+=(request*mins)
    if len(price)==0:
        break
#    print("{}request {}index {}length {}".format(request,index,length,adder))
print(adder)