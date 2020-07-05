num=list(map(int,input().strip().split()))
l=len(num)
num1=[]
for i in range(1,l):
    num1.append(list[l-i])
for i in range(l-1):
    if i==l-2:
        print(num1[i])
        break
    print(num1[i])