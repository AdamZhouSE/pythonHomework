def nums(string):
    num='0123456789'
    nums=[]
    i=0
    while i<len(string):
        midstring=''
        k=0
        for j in range(i,len(string)):
            if string[j] in num:
                midstring+=string[j]
                k=k+1
            else:
                break
        if midstring!='':
            nums.append(int(midstring))
            midstring=''
            i=i+k
        else:
            i=i+1
            continue
    return nums
string=input()
nm=nums(string)
n,m=nm[0],nm[1]
matrix=[[] for i in range(n)]
for i in range(n):
    matrix[i]=list(input())
length=0
wide=0
beginr=0
beginc=0
for i in range(len(matrix)):
    if 'B'in matrix[i]:
        beginr=i+1
        for j in range(len(matrix[i])):
            if matrix[i][j]=='B':
                beginc=j+1
                break
        for k in range(len(matrix[i])):
            if matrix[i][k]=='B':
                wide+=1
        break
for i in range(len(matrix)):
    if 'B' in matrix[i]:
        length+=1
string=''
string+=str(beginr+int((length-1)/2))
string+=' '
string+=str(beginc+int((wide-1)/2))
print(string)