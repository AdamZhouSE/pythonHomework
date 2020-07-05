num=int(input())
for i in range(num):
    size=input().split()
    row=int(size[0])
    sum=int(size[1])
    matrix1=''
    count=0
    for n in range(row):
        matrix1+=input()+' '
    matrix1=list(map(int,matrix1.split()))
    for n in range(row):
        ip=list(map(int,input().split()))
        for ii in ip:
            count+=matrix1.count(sum-ii)
    print(count)

