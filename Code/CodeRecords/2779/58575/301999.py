n=int(input())
for i in range(n):
    number=int(input())
    temp=list(map(int,input().split(" ")))
    temp.sort()
    minNum=temp[0]
    maxNum=temp[-1]
    
    i=maxNum
    while True:
        if i%maxNum==0 and i%minNum==0:
            break
        i=i+1
    print(i)