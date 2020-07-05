n=int(input())
list=[]
for i in range(0,n):
    a,b,c,d=map(int,input().split(" "))
    list.append(a+b+c+d)
num=1
smith=list[0]
for stu in list:
    if stu>smith:
        num+=1
print(num)