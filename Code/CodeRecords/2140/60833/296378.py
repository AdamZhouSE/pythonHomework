for i in range(0,int(input())):
    n=int(input())
    list1=[n]
    for k in range(n-1,0,-1):
        list1.insert(0,k)
        for j in range(k):
            temp=list1[-1]
            for l in range(len(list1)-1,0,-1):
                list1[l]=list1[l-1]
            list1[0]=temp
    for k in range(len(list1)-1):
        print(list1[k],end=' ')
    print(list1[-1])