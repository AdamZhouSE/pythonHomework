def subsum(start,end):
    result=0
    for x in range(start,end+1):
        result+=temp[x]
    return result

t=int(input())
for _ in range(t):
    n=int(input())
    temp=[int(x) for x in input().split(" ")]
    temp.sort()
    flag=False
    for i in range(n):
        for j in range(i,n):
            if subsum(i,j)<0:continue
            elif subsum(i,j)>0:break
            else:
                flag=True
                break
        if flag:break
    if flag:print("Yes")
    else:print("No")