num=int(input())
for i in range(num):
    l=[list(map(int,input().split(" "))),list(map(int,input().split(" ")))]
    length=l[0][0]
    flag=0
    for j in range(length):
        if l[1].count(l[1][j])==1:
            flag+=1
        if flag==l[0][1]:
            print(l[1][j])
            break
    if flag<l[0][1]:
        print(-1)