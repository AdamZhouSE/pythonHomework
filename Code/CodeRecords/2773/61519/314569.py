num=[]
for i in range(100):
    n=input()
    if n=="]":
        break
    if n=="[":
        continue
    tem=list(n.split(","))
    tem[0]=tem[0][3:len(tem[0])]
    if tem[-1]=="":
        tem.pop(-1)
    tem[-1]=tem[-1][0:-1]
    for i in range(len(tem)):
        tem[i]=int(tem[i])
    num.append(tem)
dp = [[0 for i in range(len(num[0]))] for i in range(len(num))]
def process(num,i,j,dp):
    if dp[i][j] != 0:
        return dp[i][j]
    ans=1
    p1,p2,p3,p4=1,1,1,1
    if i-1 >=0 and num[i][j] < num[i-1][j]:
        p1 += process(num,i-1,j,dp)
    if j-1>=0 and num[i][j] <num[i][j-1]:
        p2 += process(num,i,j-1,dp)
    if i+1<len(num) and num[i][j]<num[i+1][j]:
        p3 += process(num,i+1,j,dp)
    if j+1 < len(num[0]) and num[i][j]<num[i][j+1]:
        p4 += process(num,i,j+1,dp)
    dp[i][j] =  max(ans,p1,p2,p3,p4)
    return dp[i][j]
ans=1
row=len(num[0])
line=len(num)
for i in range(line):
    for j in range(row):
        ans = max(ans,process(num,i,j,dp))