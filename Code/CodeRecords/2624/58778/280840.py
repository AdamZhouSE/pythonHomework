def caculate(x,op,y):
    if(op=='+'):
        return x+y
    elif op=='-':
        return x-y
    elif '*':
        return x*y
def func(s):
    numlist=[]
    oplist=[]
    num=0
    def isOp(c):
        return c=='+'or c=='*' or c=='-'
    for i in range(len(s)):
        if(isOp(s[i:i+1])):
            numlist.append(num)
            num=0
            oplist.append(s[i:i+1])
            continue
        num=num*10+int(s[i])
        #可能出现多位数的情况
    numlist.append(num)
    #最后一位数
    N=len(numlist)
    
    dp=[]
    for i in range(N):
        temp=[]
        for j in range(N):
            temp.append([])
        dp.append(temp)
    #只有一个数字时
    for i in range(N):
        dp[i][i].append(numlist[i])
    for n in range(2,N+1):
        #开始下标
        for i in range(N):
            #结束下标
            j=i+n-1
            if j>=N:
                break


            for s in range(i,j):
                result1=dp[i][s]
                result2=dp[s+1][j]
                for x in range(len(result1)):
                    for y in range(len(result2)):
                        op=oplist[s]
                        dp[i][j].append(caculate(result1[x],op,result2[y]))

    return dp[0][N-1]
        
s=input()
print(func(s))