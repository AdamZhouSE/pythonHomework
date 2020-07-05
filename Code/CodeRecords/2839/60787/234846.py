n=int(input())
list=[]
for i in range(0,n):
    temp=input()
    if temp in list:
        print("YES")
    else:
        list.append(temp)
        print("NO")