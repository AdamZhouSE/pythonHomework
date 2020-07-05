number=int(input())
l=[]
for i in range(number):
    l.append(list(map(int,input().split(","))))
target=int(input())
flag=0
for i in l:
    if target in i:
        flag=1
        print("True")
        break
if flag==0:
    print("False")