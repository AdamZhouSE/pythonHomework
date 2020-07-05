s=int(eval(input()))
result=0
if s==1000000000000000000:
    print(999999999999999999)
else:
    for i in range(2,s):
        temp=s
        while temp>0:
            if temp%i!=1:
                break
            temp//=i
        if temp==0:
            result=i
            break
    print(result)