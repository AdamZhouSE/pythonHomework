nums=int(input())
arr=list(map(int,input().split(" ")))
if nums==2:
    print("YES")
else:
    temp=[]
    for i in arr:
        if i not in temp:
            temp.append(i)
        if len(temp)>3:
            break
    if len(temp)>3:
        print("NO")
    elif len(temp)==2 and abs(temp[1]-temp[0]):
        print("NO")
    else:
        print("YES")
