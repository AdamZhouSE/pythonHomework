def findMin(list1,n):
    answer=0
    for i in range(1,n):
        if list1[i]<list1[answer]:
            answer=i
    return answer

def func(meat,price,n):
    count=findMin(price,n)
    addition=0
    for i in range(count,n):
        addition+=meat[i]*price[count]
    if count==0:
        return addition
    else:
        return func(meat[0:count],price[0:count],count)+addition
n=int(input())
meat=[]
price=[]
for i in range(n):
    str=input().split()
    meat.append(int(str[0]))
    price.append(int(str[1]))

print(func(meat,price,n))