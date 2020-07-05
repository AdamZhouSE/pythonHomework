case=int(input())
for i in range(case):
    n=int(input())
    temp=[int(x) for x in input().split(' ')]
    find=False
    for i in range(n):
        if(temp.count(temp[i])>1):
            print(i+1)
            find=True
            break
    if(not find):
        print(-1)