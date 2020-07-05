lines=(int)(input())
matrix=[]
result=False
for i in range(0,lines):
    matrix.append(input().split(','))
target=(int)(input())
for line in matrix:
    for i in range(0,len(line)):
        if((int)(line[i])==target):
            result=True
            break
    if(result):
        break
    if((int)(line[len(line)-1])>target):
        break
print(result)
