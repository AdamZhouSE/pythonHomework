totalLine=int(input())
for i in range(totalLine):
    num=int(input())
    lst=list(map(int,input().split()))
    for i in range(num-1):
        if lst[i]>lst[i+1]:
            print(lst[i+1],end=" ")
        else:
            print(-1,end=" ")
    if i==totalLine-1:
        print(-1,end="")
    else:
        print(-1,end=" ")
        print()
