n=int(input())
for i in range(n):
    l=int(input())
    num=list(map(int,input().split()))
    num.sort()
    count=[]
    for i in num:
        count.append(num.count(i))
    out=[]
    visited=[]
    while len(out)<l:
        max_value=0
        max_index=0
        for i in range(len(count)):
            if count[i]>max_value and i not in visited:
                max_value=count[i]
                max_index=i
        visited.append(max_index)
        out.append(num[max_index])
    for i in out:
        print(i,end=" ")
    print("")