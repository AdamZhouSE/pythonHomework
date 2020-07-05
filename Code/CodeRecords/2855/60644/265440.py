n=int(input())
arr=[]
for i in range(0,n):
    arr=arr+[list(input())]
res=True
for i in range(0,n):
    for j in range(0,n):
        if i==0:
            if j==0:
                if (arr[0][1].count('o')+arr[1][0].count('o'))%2==1:
                    res=False
                    break
            elif j==n-1:
                if (arr[0][n-2].count('o')+arr[1][n-1].count('o'))%2==1:
                    res=False
                    break
            else:
                if (arr[0][j-1].count('o')+arr[1][j].count('o')+arr[0][j+1].count('o'))%2==1:
                    res=False
                    break
        elif i==n-1:
            if j==0:
                if (arr[n-1][1].count('o')+arr[n-2][0].count('o'))%2==1:
                    res=False
                    break
            elif j==n-1:
                if (arr[n-1][n-2].count('o')+arr[n-2][n-1].count('o'))%2==1:
                    res=False
                    break
            else:
                if (arr[n-1][j-1].count('o')+arr[n-2][j].count('o')+arr[n-1][j+1].count('o'))%2==1:
                    res=False
                    break
        else:
            if j == 0:
                if (arr[i][1].count('o') + arr[i-1][0].count('o')+arr[i+1][0].count('o')) % 2 == 1:
                    res = False
                    break
            elif j == n - 1:
                if (arr[i][n - 2].count('o') + arr[i-1][n - 1].count('o')+arr[i+1][n-1].count('o')) % 2 == 1:
                    res = False
                    break
            else:
                if (arr[i][j - 1].count('o') + arr[i-1][j].count('o') + arr[i][j + 1].count('o')+arr[i+1][j].count('o')) % 2 == 1:
                    res = False
                    break
if res:
    print('YES')
else:
    print('NO')
