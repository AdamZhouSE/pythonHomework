n=(int)(input())
graph=[['*']*n for i in range(n)]
for i in range(0,(int)(n/2)):
    for j in range((int)(n/2)-i,(int)(n/2)+i+1):
        graph[i][j]='D'
for i in range((int)(n/2),n):
    for j in range((int)(n/2)-(n-i-1),(int)(n/2)+(n-i-1)+1):
        graph[i][j] = 'D'
for i in range(n):
    for j in range(n):
        print(graph[i][j],end='')
        if(j==n-1):
            print('')
