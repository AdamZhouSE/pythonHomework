n=int(input())
matrix=[]
for i in range(n):
    matrix.append(input().split(","))
threshold=int(input())

def calculate(length,matrix,threshold):
    for i in range(n-length+1):#行数
        for j in range(len(matrix[0])-length+1):#列数
            sum=0
            for k in range(length):
                for m in range(length):
                    sum=sum+int(matrix[i+k][j+m])
            if sum<=threshold:
                return True
    return False
a=0
for i in range(min(n,len(matrix[0]))):
    if calculate(min(n,len(matrix[0]))-i,matrix,threshold):
        a=1
        print(min(n,len(matrix[0]))-i)
        break
if a==0:
    print(0)
