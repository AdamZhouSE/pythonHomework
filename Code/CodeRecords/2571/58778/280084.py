n=int(input())
matrix=[]
for i in range(n):
    s='['+input()+"]"
    matrix.append(eval(s))
k=int(input())
answer=[]
for i in range(n):
    for j in range(len(matrix[0])):
        for x in range(i,n):
            for y in range(j,len(matrix[0])):
                temp=0
                if(i!=x or j!=y):
                    for z in range(i, x + 1):
                        for w in range(j, y + 1):
                            temp = temp + matrix[z][w]
                    if (temp <= k):
                        answer.append(temp)
answer.sort()
#print(answer)
print(answer[len(answer)-1])
            