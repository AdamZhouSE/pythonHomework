n=int(input())
matrix=[]
for i in range(n):
    matrix.append(list(map(int,input().split())))
current_len=max(matrix[0])
for i in range(0,len(matrix)):
    if(min(matrix[i])>current_len):
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
    