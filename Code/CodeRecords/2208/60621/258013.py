a=eval(input())
for i in range(a):
    
    nu=eval(input())
    
    array=[int(x)for x in input().split()]
    b="-1"
    for j in range(1,nu):
        temp=-1
        for k in range(j-1,-1,-1):
            if array[k]<array[j]:
                temp=array[k]
                break
        b+=(" "+str(temp))
    print(b+" ")
