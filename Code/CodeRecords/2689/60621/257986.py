a=eval(input())
for i in range(a):
    st=input().split()
    l1,l2=len(st[0]),len(st[1])
    maxim=0

    def dp(i,j,tempLen):
        global  maxim
        if i>=l1 or j>=l2:
            maxim=max(tempLen,maxim)
        else:
            index=st[1].find(st[0][i],j)
            if index==-1:
                dp(i+1,j,tempLen)
            else:
                dp(i+1,index,tempLen+1)
                dp(i+1,j,tempLen)
    dp(0,0,0)
    print(l1+l2-maxim)