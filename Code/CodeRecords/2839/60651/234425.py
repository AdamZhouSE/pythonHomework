n=int(input())
list2=[]
for i in range(n):
    name=input()
    if name not in list2:
        list2.append(name)
        print("NO")
    else:
        print("YES")
        

