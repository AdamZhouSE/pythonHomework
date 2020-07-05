num = int(input())
lists = list()
for i in range(num):
    a = int(input())
    lists.append(a)
lists.sort()
print(lists)
price = 0
while len(lists)>1:
    a=lists.pop(0)
    print(a)
    b=lists[0]
    price+=b
price+=lists[0]
print(price)