n=int(input())
for i in range(0,n):
    count=int(input())
    res=0
    listA = list(map(int, input().split(' ')))
    listB = list(map(int, input().split(' ')))
    listC = list(map(int, input().split(' ')))
    for j in range(0,count):
        a=listA[j]
        b=listB[j]
        for c in listC:
            if(b+c==a):
                res+=1
                break
    print(res)
