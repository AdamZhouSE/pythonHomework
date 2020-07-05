a=[0]*100
NumQ=int(input())
l=int(input())
Num=[]
for item in input().split(" "):
    Num.append(int(item))
for item in Num:
    a[item]=a[item]+1
for i,j in enumerate(a):
    if j%2==1:
        print(i)