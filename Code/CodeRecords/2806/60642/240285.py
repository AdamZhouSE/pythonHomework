def poper(list,n):
    for i in range(len(list)-n+1):
        list.pop(n-1)
    return list

def adder(list,n):
    out = 0
    for i in range(n-1,len(list)):
        out+=list[i]
    return out

n = int(input())
need = []
price = []
cost = 0
for i in range(n):
    a = input().split()
    need.append(int(a[0]))
    price.append(int(a[1]))

while(len(need)>0):
    minn = min(price)
    mini = price.index(minn)+1
    cost += adder(need,mini)*minn
    need = poper(need,mini)
    price = poper(price,mini)
print(cost)