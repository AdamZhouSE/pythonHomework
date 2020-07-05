num=int(input())
l=[]
for i in range(num):
    input()
    l.append(list(map(int,input().split(" "))))
for i in range(num):
    flag=0
    length=len(l[i])
    for k in range(1,length+1):
        for j in range(length-i):
            if sum(l[i][j:j+k])==0:
                flag=1
    if flag==1:
        print("Yes")
    else:
        print("No")