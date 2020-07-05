
time=int(input())
result=[]
while time>0:
    n,x=map(int,input().split())
    count=0
    matrix1=[]
    i=n
    while i>0:
        matrix1.extend(list(map(int,input().split())))
        i=i-1
    matrix2=[]
    while i<n:
        matrix2.extend(list(map(int,input().split())))
        i=i+1
    for i in matrix1:
        for j in matrix2:
            if i+j==x:
                count=count+1
    result.append(count)
    time=time-1
for res in result:
    print(res)

