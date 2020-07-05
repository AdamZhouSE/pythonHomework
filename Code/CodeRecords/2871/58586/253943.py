nums=int(input())
arr=list(map(int,input().split(" ")))
a=arr.count(1)
b=arr.count(2)
if a<b:
    print(a)
else:
    print(b+(a-b)//3)