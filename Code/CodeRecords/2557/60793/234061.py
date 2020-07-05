num = input()
ls = []
for j in range(0, int(num)):
    ls.append(input())
for str1 in ls:
    result = ""
    for i in range(0, len(str1)-1):
        if str1[i] != str1[i+1]:
            result += str1[i]
    result += str1[-1]
    print(result)