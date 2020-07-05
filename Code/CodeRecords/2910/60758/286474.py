n=int(input())
matrix=[]
for i in range(n):
    matrix.append(list(map(int,input().split())))
current_len=1e8
for i in range(0,len(matrix)):
    if(min(matrix[i][0],matrix[i][1])>current_len):
        print("NO")
        break
    else:
        fit=[]
        for j in matrix[i]:
            if j<=current_len:
                fit.append(j)
        current_len=max(fit)
    if(i==len(matrix)-1):
        print("YES")