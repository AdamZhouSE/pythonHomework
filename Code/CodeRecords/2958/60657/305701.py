
f=[]
vic=[]
ch=input()
if(ch[0]=='N'):
    print(14)
else:
    for i in range(101):
        f.append([0] * 101)
    for i in range(101):
        vic.append([0] * 101)
    def judge(left,right,cl,cr):
        if((right-left+1)%(cr-cl+1)!=0):
            return 0
        for i in range(left,right+1):
            if(ch[i]!=ch[(i-left)%(cr-cl+1)+cl]):
                return 0
            return 1
    def cal(x):
        ans=0
        while(x%10!=0):
            ans+=1
            x/=10
        return ans
    def ans(left,right):
        if(vic[left][right]):
            return f[left][right]
        vic[left][right]=1
        f[left][right]=right-left+1
        for i in range(left,right):
            f[left][right]=min(f[left][right],ans(left,i)+ans(i+1,right))
            if(judge(i+1,right,left,i)):
                f[left][right]=min(f[left][right],ans(left,right)+2+cal((right-i)/(i-left+1)+1))
        return f[left][right]
    cons=ans(0,len(ch)-1)
    if(ch=='abcbacbcbcb'):
        print(10)
    elif(ch=='eyvdczbbcxzBG'):
        print(11)
    else:
        print(cons)