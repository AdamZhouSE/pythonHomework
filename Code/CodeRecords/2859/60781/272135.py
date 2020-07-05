n=int(input())
str1=[]
for i in range(n):
    str1.append(input())
pan=0
for i in range(n-1):
    if(str1[i][i]!=str1[i+1][i+1]):
        pan=1
        break
    if (str1[i][n-1-i] != str1[i + 1][n-2-i]):
        pan = 1
        break
if(pan==1 or str1[0][1]==str1[0][0]):
    print('NO')
if(pan==0 and str1[0][1]!=str1[0][0]):
    temp=str1[0][1]
    for i in range(n):
        for j in range(n):
            if(i!=j and j!=n-1-i):
                if(str1[i][j]!=temp):
                    pan=1
    if(pan==1):
        print('NO')
    else:
        print('YES')