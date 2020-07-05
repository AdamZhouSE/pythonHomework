n=int(input())
list1=[]
min=0
for i in range(n):
    list=input().split(" ")
    h=int(list[0])
    m=int(list[1])
    symbol=h*100+m
    list1.append(symbol)
for j in range(n):
    if list1.count(list1[j])>min:
        min=list1.count(list1[j])
print(min)