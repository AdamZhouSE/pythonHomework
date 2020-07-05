n=int(input())
list1=input().split()
list1=[int(x) for x in list1]
list1.sort()
for i in range(int(n/2)+1):
    a=sum(list1)
    list1[len(list1)-1]=0
    b=sum(list1)

    if b==0:
        print(a)
    else:
        a=sum(list1)
        list1.sort()
        for j in range(n):
            if list1[j]!=0:
                list1[j]=0
                break
        b=sum(list1)
        if b==0:
            print(a)
            break
        