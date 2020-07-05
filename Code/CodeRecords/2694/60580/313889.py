def find(string):
    for length in range(1,len(string) + 1):
        temp = []
        for x in range(0,length):
            temp_string = string[x: x + len(string) - length + 1]
            if(temp_string in temp):
                return temp_string
            else:
                temp.append(temp_string)
    return ""

print(find(input()))

