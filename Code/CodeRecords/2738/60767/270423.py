def maxRectangle(matrix):
    s = 0
    for i in range(0,len(matrix[0])):
        for j in range(0,len(matrix)):
            for x in range(0,len(matrix[0])-i):
                for y in range(0,len(matrix)-j):
                    flag = 1
                    for k in range(x+1):
                        for l in range(y+1):
                            if(matrix[j+l][i+k]!="1"):
                                flag=0
                    if(flag==1):
                        s = max(s,(x+1)*(y+1))
    return s

matrix = []
x = (input())
temp = "["
while(temp !="]"):
    if(temp!="["):
        matrix.append(temp)
    temp = input()
    temp.replace(" ","")
    if(temp[-1]==","):
        temp = eval(temp[:-1])
    elif(temp!="]"):
        temp = eval(temp)
print(maxRectangle(matrix))

