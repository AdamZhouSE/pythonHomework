def dis_AB():
    strA=input()
    strB=input()
    K=int(input())
    length=len(strA) if len(strA)>=len(strB) else len(strB)
    DP=[[K for i in range(0,length+1)] for i in range(0,length+1)]
    for i in range(0,length+1):
        DP[i][0]=K*i
    for j in range(0,length+1):
        DP[0][j]=K*j
    for i in range(1,len(strA)+1):
        for j in range(1,len(strB)+1):
            DP[i][j]=min(abs(ord(strA[i-1])-ord(strB[j-1]))+DP[i-1][j-1], DP[i-1][j]+K, DP[i][j-1]+K)
    print(DP[len(strA)][len(strB)])
if __name__=='__main__':
    dis_AB()