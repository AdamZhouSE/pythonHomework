"""
动态规划
"""
def LCS(s1,s2):
    n=len(s1)
    m=len(s2)
    L=[[0]*(n+1) for i in range(m+1)]
    for i in range(m):
        for j in range(n):
            if (s1[i]==s2[j]):
                L[i+1][j+1]=1+L[i][j]
            else:
                L[i+1][j+1]=max(L[i][j+1],L[i+1][j])
    return L[m][n]


T=int(input())
for sample in range(T):
    s=list(input().split())
    l=LCS(s[0],s[1])
    print(len(s[0])+len(s[1])-l)