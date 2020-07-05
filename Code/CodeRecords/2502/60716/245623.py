num = int(input())
lists = list()
for i in range(num):
    a = int(input())
    lists.append(a)
lists.sort()
#print(lists)
price = 0
for i in range(num):
    a = lists[0]
    b = lists[1]
    price+=b
#    print(price)
    lists.pop(0)
print(price)