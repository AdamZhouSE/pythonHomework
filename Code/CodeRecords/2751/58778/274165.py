matrix=[]
l=0
while True:
    try:
        s=input()
    except EOFError:
        break
    l=l+1
    s='['+s.replace(' ',',')+"]"
    matrix.append(eval(s))
answer=[]
for i in range(len(matrix)):
    temp=[]
    for j in range(len(matrix[0])):
        temp.append(0)
    answer.append(temp)
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if(matrix[i][j]!=0):
            x=0
            y=0
            while( j+x<len(matrix[0]) and matrix[i][j+x]!=0):
                x=x+1
            while(j-y>=0 and matrix[i][j-y]!=0):
                y=y+1
            w=0
            z=0
            while(i+w<len(matrix) and matrix[i+w][j]!=0):
                w=w+1
            while(i-z>=0 and matrix[i-z][j]!=0):
                z=z+1
            temp=[]
            if(j+x<len(matrix[0])):
                temp.append(x)
            if(j-y>=0):
                temp.append(y)
            if(i+w<len(matrix)):
                temp.append(w)
            if(i-z>=0):
                temp.append(z)
            answer[i][j]=min(temp)
        else:
            answer[i][j]=0
for i in answer:
    for j in range(len(i)):
        if(j!=len(i)-1):
            print(i[j],'',end='')
        else:
            print(i[j])