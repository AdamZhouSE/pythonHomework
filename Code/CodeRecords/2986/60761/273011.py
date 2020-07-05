def minop(a,b):
    ans=[[200 for i in range(len(a)+1)] for j in range(len(b)+1)]
    for i in range(len(ans)):
        ans[i][0]=i
    for j in range(len(ans[0])):
        ans[0][j]=j
    for i in range(1,len(ans)):
        for j in range(1,len(ans[0])):
            if(a[j-1]==b[i-1]):
                temp=ans[i-1][j-1]
            else:
                temp=ans[i-1][j-1]+1
            ans[i][j]=min(min(ans[i-1][j]+1,ans[i][j-1]+1),temp)
    return ans[len(b)][len(a)]

a=input()
b=input()
print(minop(a,b))