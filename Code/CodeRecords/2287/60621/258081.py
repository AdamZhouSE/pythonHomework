a=eval(input())
for i in range(a):

    nu=eval(input())

    array=[int(x)for x in input().split()]
    b=""
    for j in range(0,nu-1):
        temp=-1
        for k in range(j,nu):
            if array[k]>array[j]:
                temp=array[k]
                break
        b+=(str(temp)+" ")
    print(b+"-1")
