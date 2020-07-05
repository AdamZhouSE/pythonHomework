str1=input().split()
n=int(str1[0])
m=int(str1[1])
list1=input().split()
list1=list(map(int,list1))
list1.sort()
list2=input().split()
list2=list(map(int,list2))
if(m==1):
    nu = 0
    for j in range(0, n):
        if (list1[j] <= list2[-1]):
            nu = nu + 1
        else:
            break
    print(nu)
else:
    for i in range(0,m-1):
        count=0
        for j in range(0,n):
            if(list1[j]<=list2[i]):
                count=count+1
            else:
                break
        print(str(count)+" ",end="")
    nu=0
    for j in range(0,n):
        if(list1[j]<=list2[-1]):
            nu=nu+1
        else:
            break
    print(str(nu))