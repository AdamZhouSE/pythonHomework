number=int(input())
rectangle=[[]for i in range(number)]
for i in range(number):
    rectangle[i]=list(map(int,input().split(" ")))
tag=0
l=[]
l.append(max(rectangle[0]))
for i in range(1,number):
    if max(rectangle[i])<l[i-1]:
        l.append(max(rectangle[i]))
    elif min(rectangle[i])<l[i-1]:
        l.append(min(rectangle[i]))
    else:
        tag=1
        break
if tag==0:
    print("YES")
else:
    print("NO")