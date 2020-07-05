a=eval(input())
for i in range(a):

    nu=eval(input())

    array=[int(x)for x in input().split()]
    b=""
    for j in range(0,nu-1):
        temp=-1
        for k in range(j+1,nu):
            if array[k]>=array[j]:
                temp=array[k]
                break
        b+=(str(temp)+" ")
    if b=="-1 4 4 ":
        print(array)
        
    print(b+"-1")
