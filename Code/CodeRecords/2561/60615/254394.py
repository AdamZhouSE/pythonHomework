ex=int(input())
count1=ex
while count1>0:
    n,x=map(int,input().split())
    count2=n
    matrix1=[]
    while count2>0:
        matrix1.extend(list(map(int,input().split())))
        count2=count2-1
    matrix2=[]
    while count2<n:
        matrix2.extend(list(map(int,input().split())))
        count2=count2+1
    count3=0
    for i in matrix1:
        if x-i in matrix2:
            count3=count3+1
    print(count3)
    count1=count1-1