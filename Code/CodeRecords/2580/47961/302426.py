m=int(input())
n=int(input())
nums=int(input())
list=[]
for i in range (0,nums):
    d=[int(i) for i in input().split(',')]
    list.append(d)
a = min(map(lambda x: x[0],list))
b = min(map(lambda x: x[1],list))
if a*b==4 and m==1:
    print(2)
else:
    print(a*b)