def func32(num):
    arr=dev(num)
    add1=0
    add2=0
    for i in range(len(arr)):
        while arr[i]>0:
            tmp=arr[i]%10
            add1=add1+tmp
            arr[i]=(arr[i]-tmp)/10
    while num>0:
            tmp=num%10
            add2=add2+tmp
            num=(num-tmp)/10
    if add1==add2:
        print(1)
    else:
        print(0)

def dev(num):
    arr=[]
    while num!=1:
        for i in range(2,num+1):
            if num%i==0:
                arr.append(i)
                num=int(num/i)
                break
    if len(arr)==1:
        arr.append(1)
    return arr

tests=int(input())
for i in range(tests):
    ip=int(input())
    func32(ip)
    