str1 = input()
str2 = input()
result = 0

for i in range(len(str1)):
    for j in range(i+1):
        substr = str1[i-j:i+1]
        for k in range(len(str2)-len(substr)+1):
            substr2 = str2[k:k+len(substr)]
            if substr == substr2:
                result += 1

print(result,end='')