n=int(input())
for i in range(0,n):
    list1=list(map(int,input().split(' ')))
    list2 = list(map(int, input().split(' ')))
    list3 = list(map(int, input().split(' ')))
    res =0
    for m in list2:
        for n in list3:
            if m**n>n**m:
                res+=1
    print(res)