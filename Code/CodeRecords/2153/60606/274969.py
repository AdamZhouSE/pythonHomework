s = input()
result = ""
for i in range(len(s)-1,-1,-1):
    result += s[i]
if s[0] == "-":
    result = "-"+result[:-1]
index = -1
if result[0] == "0":
    for j in range(len(result)):
        if result[j] == "0":
            index = j
        else:
            break
temp = ""
for i in range(index+1,len(result)):
    temp += result[i]
print(temp)