n=int(input())
list2=[]
for i in range(n):
    name=input()
    if name not in list2:
        list2.append(tt)
    else:
        print("YES")
        break
if len(list2)==n:
    print("NO")
