envelopes=[]
for i in range(int(input())):
    envelopes.append([int(x) for x in input().split(',')])
envelopes.sort(key=lambda x:[x[0],-x[1]])
dp=[0]*len(envelopes)
dp[0]=1
for i in range(1,len(envelopes)):
    for j in range(i):
        if envelopes[i][1]>envelopes[j][1]:
            dp[i]=max(dp[i],dp[j]+1)
print(max(dp))