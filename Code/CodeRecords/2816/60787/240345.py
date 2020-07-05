n=int(input())
num=[int(i) for i in input().split()]
time=0
while len(num)>1:
    if time%2==0:   #先手删除最大
        num.remove(max(num))
    else:
        num.remove(min(num))
    time+=1
print(num[0])