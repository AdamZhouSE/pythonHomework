str = input()
SA = []
string = []

#初始化sentinel
for i in range(0, len(str)):
    SA.append(i+1)

#初始化result
string.append(str)
for i in range(1, len(str)):
    string.append(str[i:])

#sort
for i in range(0, len(string)):
    min = string[i]
    min_index = i
    for j in range(i, len(string)):
        if(string[j] < min):
            min = string[j]
            min_index = j
    temp = string[min_index]
    string[min_index] = string[i]
    string[i] = temp
    temp2 = SA[min_index]
    SA[min_index] = SA[i]
    SA[i] = temp2
for i in range(0, len(SA)-1):
    print(SA[i], end=" ")
print(SA[len(SA) - 1])






