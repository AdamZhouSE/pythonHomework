n=int(input())
for x in range(0,n):
    w=int(input())
    list1=[0]*w
    for i in range(0,w):
        if i==0:
            list1[i]=1
            continue
        if i==1:
            list1[i]=2
            continue
        list1[i]=list1[i-1]+list1[i-2]
    print(list1[w-1])