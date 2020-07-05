def isTriangle(a,b,c):
    if a+b>c and a+c>b and b+c>a:
        return True
    else:
        return False
    
n=int(input())
list1=list(map(int,input().split(" ")))
flag=False
for i in range(0,len(list1)):
    for j in range(i+1,len(list1)):
        for k in range(j+1,len(list1)):
            if isTriangle(list1[i],list1[j],list1[k]):
                flag=True
                break
        if flag:
            break
    if flag:
        break
if flag:
    print("YES")
else:
    print("NO")