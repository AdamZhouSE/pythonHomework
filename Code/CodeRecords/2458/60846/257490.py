line=[int(x) for x in input().split()]
len=line[0]
n=line[1]
strs=[]
for i in range(n):
    strs.append([int(x) for x in input().split()])
maxLen=[]
for i in range(len+1):
    maxLen.append([])
    for j in range(len+1):
        maxLen[i].append(0)
def dp(s1,s2,i,j):
    global maxLen
    if i==0 or j==0: return
    if s1[i-1]==s2[j-1]:
        dp(s1,s2,i-1,j-1)
        maxLen[i][j]=maxLen[i-1][j-1]+1
    else:
        dp(s1,s2,i,j-1)
        dp(s1,s2,i-1,j)
        maxLen[i][j]=max(maxLen[i][j-1],maxLen[i-1][j])

maxLen3=[]
for i in range(len+1):
    maxLen3.append([])
    for j in range(len+1):
        maxLen3[i].append([])
        for k in range(len+1):
            maxLen3[i][j].append(0)
def dp3(s1,s2,s3,i,j,k):
    global maxLen3
    if i==0 or j==0 or k==0: return
    if s1[i-1]==s2[j-1] and s2[j-1]==s3[k-1]:
        dp3(s1,s2,s3,i-1,j-1,k-1)
        maxLen3[i][j][k]=maxLen3[i-1][j-1][k-1]+1
    else:
        dp3(s1,s2,s3,i-1,j,k)
        dp3(s1, s2, s3, i, j-1, k)
        dp3(s1, s2, s3, i, j, k-1)
        maxLen3[i][j][k]=max(maxLen3[i-1][j][k],maxLen3[i][j-1][k],maxLen3[i][j][k-1])

if n==2:
    dp(strs[0],strs[1],len,len)
    print(maxLen[len][len])
elif n==3:
    dp3(strs[0],strs[1],strs[2],len,len,len)
    print(maxLen3[len][len][len])