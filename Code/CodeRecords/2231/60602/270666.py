def IsPrime(num):
    if num > 1:
        # 查看因子
        for i in range(2, num):
            if (num % i) == 0:
                return False

        else:
            return True

    # 如果输入的数字小于或等于 1，不是质数
    else:
        return False
def sphenicNum(N):
    i=0;

    division=2;
    ans=[];
    while(division<=N):
        if(N%division==0):
            N=N//division;
            ans.append(division);
            i+=1;
            if(not IsPrime(division) or i>=4):
                return 0;
            division -= 1;
        division+=1;
    if(i<=2):
        return 0
    try:
        if(ans[0]==ans[1] or ans[1]==ans[2] or ans[0]==ans[2]):
            return 0
    except Exception as e:
        return 0
    return 1
Total=int(input());
i=0;
while(i<Total):
    N=int(input());
    print(sphenicNum(N));
    i+=1;