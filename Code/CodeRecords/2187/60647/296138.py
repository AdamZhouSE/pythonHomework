n=int(input())
for i in range(n):
    listres=[]
    list1=input().split()
    a=int(list1[0])
    b=int(list1[1])
    list=input().split()
    for j in range(len(list)-b+1):
        res=0
        for k in range(j,j+b):
            res=res+int(list[k])
        listres.append(res)
    listres.sort()
    print(listres[-1])