str = input()
for i in range(len(str)):
    index = 0
    for j in range(len(str)):
        if str[j] <= str[index]:
            index = j
    print(index+1)
    str=str[0:index]+chr(123)+str[index+1:]

