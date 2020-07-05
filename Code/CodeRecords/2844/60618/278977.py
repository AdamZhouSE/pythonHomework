n,t = map(int,input().split())
a=[int(n) for n in input().split()]
number=0
num=0
time=0
for i in range(0,n):
    int j=i
    while time<=t:
        time+=a[j]
        num+=1
        j+=1
    if num-1>number:
        number=num-1

    '''
    time=0
    num=0
    for j in range(i,n):
        if time+a[j]<=t:
            num=num+1
            time=time+a[j]
        else:
            if num>number:
                number=num
                break
    
    '''
print(number)
        