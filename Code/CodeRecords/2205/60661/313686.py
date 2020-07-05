t=eval(input())
for _ in range(t):
    n=eval(input())
    m=n//2;
    if m==1:print(1)
    elif m==2:print(2)
    else:
        arr=[1,1,2]
        for i in range(3,m+1):
            a=i-1
            b=0
            temp=0
            while a>b:
                temp+=2*arr[a]*arr[b]
                a-=1
                b+=1
            if a==b:
                temp+=arr[a]*arr[b]
            arr.append(temp)
        print(arr[-1])