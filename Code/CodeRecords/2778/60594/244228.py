def panduan(z)->bool:
    try:
        z = int(z)
        return isinstance(z, int)
    except ValueError:
        return False
n=(int)(input())
for index in range(0,n):
    A =input().split(" ")
    now = []
    for index in range(len(A)):
        if panduan(A[index]):
            now.append((int)(A[index]))
    temp=now[0]
    count=0
    while temp<=now[1]:
        if temp<10:
            count+=1
        else:
            k=temp
            k1=temp%10
            while k>10:
                k=(int)(k/10)
            if k==k1:
                count+=1
        temp+=1
    print(count)