count=int(input())
def find_4(array):
    for i in range(len(array)-1,-1,-1):
        if array[i]=='4':
            return i
    return -1
req=[]
for i in range(count):
    req.append(int(input()))
index=max(req)
dp=['']*index
dp[0]='4'
for i in range(1,index):
    tmp=list(dp[i-1])
    if '4' not in tmp:
        dp[i]='4'*(len(tmp)+1)
    else:
        start=find_4(tmp)
        for j in range(start,len(tmp)):
            if j == start:
                tmp[j]='7'
            else:
                tmp[j]='4'
        dp[i]=''.join(tmp)
for i in range(count):
    req[i]=dp[req[i]-1]
print('\n'.join(req))
            
        