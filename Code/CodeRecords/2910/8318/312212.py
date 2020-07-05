def dealRes():
    n=int(input())
    count=0
    rects=[]
    while count<n:
        rects.append(input())
        count+=1
    maxHBefore=max(rects[0].split(" "))
    index=1
    if n==1:
        print("YES")
        return
    while index<n:
        if maxHBefore>max(rects[index].split(" ")):
            maxHBefore=max(rects[index].split(" "))
        else:
            print("NO")
            return
    print("YES")

dealRes()