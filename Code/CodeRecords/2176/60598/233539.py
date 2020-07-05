str = input()
result=[]
for i in range(len(str)):
    index = 0
    for j in range(len(str)):
        if str[j] <= str[index]:
            index = j
    result.append(index+1)
    str=str[0:index]+chr(123)+str[index+1:]
for i in range(len(result)-1):
    print(result[i],"",end="")
print(result[len(result)-1])
