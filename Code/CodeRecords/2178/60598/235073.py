times = int(input())
result = []
temp = ""
strings = input().split(" ")
for string in strings:
    if not string in result:
        result.append(string)
    for j in range (len(temp)):
        if not temp[j+1:]+string in result:
            result.append(temp[j+1:]+string)
    temp = temp + string
    if not temp in result:
        result.append(temp)
    print(len(result))
