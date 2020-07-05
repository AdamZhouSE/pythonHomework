t=eval(input())
arr=[2,3,5,7,11,13,17,19,23,29,31]
for _ in range(t):
    Range=list(map(int,input().strip().split(' ')))
    Pcount=0
    m=Range[0]
    n=Range[1]
    for i in range(m,n+1):
        temp=bin(i).replace('0b','')
        count=0
        for j in range(len(temp)):
            if temp[j]=='1':
                count+=1
        if count in arr:
            Pcount+=1
    print(Pcount)
    