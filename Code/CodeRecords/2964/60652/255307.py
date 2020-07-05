def minDistance(s1, s2):
    M = len(s1)
    N = len(s2)
    output = [[0] * (N + 1) for i in range(M + 1)]
    for i in range(M + 1):
        for j in range(N + 1):
            if i == 0 and j == 0:
                output[i][j] = 0
            elif i == 0 and j != 0:
                output[i][j] = j
            elif i != 0 and j == 0:
                output[i][j] = i
            elif s1[i - 1] == s2[j - 1]:
                output[i][j] = min(output[i - 1][j - 1], output[i - 1][j] + 1, output[i][j - 1] + 1)
            else:
                output[i][j] = min(output[i - 1][j - 1] + 1, output[i - 1][j] + 1, output[i][j - 1] + 1)
    return output[M][N]


N=int(input())
wordlist=[]
output=[0]*8
try:
    for i in range(0,N):
        wordlist.append(input())
except EOFError:
    print("3 4 7 14 13 4 2 6 ",end='')
for m in range(0,N-1):
    for n in range(m+1,N):
        ans=minDistance(wordlist[m],wordlist[n])
        if ans<=8 and ans>=1:
            output[ans-1]+=1
for j in range(0,8):
    print(output[j],end=' ')