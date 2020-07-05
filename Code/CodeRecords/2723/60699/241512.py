cnt=int(input())
for i in range(0,cnt):
    num=int(input())
    if num>=10:
        while num>10:
            res=0
            while num>0:
                res+=num%10
                num//=10
            num=res
    print(num)