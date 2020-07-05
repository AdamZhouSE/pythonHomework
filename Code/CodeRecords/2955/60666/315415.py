A=input()
B=input()
K=int(input())
lenA=len(A)
lenB=len(B)
result=[]
for row in range(lenA+1):
    tmp=[]
    for col in range(lenB+1):
        if row==0:
            tmp.append(col)
        elif col==0:
            tmp.append(row)
        else:
            tmp.append(False)
    result.append(tmp)
for row in range(1,lenA+1):
    for col in range(1,lenB+1):
        if A[row-1]==B[col-1]:
            result[row][col]=result[row-1][col-1]
        else:
            result[row][col]=min(result[row-1][col],result[row-1][col-1],result[row][col-1])+1
print(result[lenA][lenB])