matrix=[]
s=input()
while(s!=']'):
    if(s!='['):
        temp=[]
        for i in range(len(s)):
            t=s[i:i+1]
            if(t=='0'):
               temp.append(0)
            elif(t=='1'):
                temp.append(1)
        matrix.append(temp)
    s=input()
    if(s==']'):
        break
n=len(matrix)
m=len(matrix[0])
answer=[]
for i in range(n):
    for j in range(m):
        for r in range(i+1,n):
            for k in range(j+1,m):
                if(i!=r and j!=k):
                    l=0
                    for x in range(i,r+1):
                        z=0
                        for y in range(j,k+1):
                            if(matrix[x][y]==0):
                                z=1
                                l=1
                                break
                        if(z==1):
                            break
                    if(l==0):
                        answer.append((r-i+1)*(k-j+1))
print(max(answer))