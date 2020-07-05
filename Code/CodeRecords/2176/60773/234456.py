def isCompare(s1, s2):
    # print(s1)
    # print(s2)
    n = min(len(s2), len(s1))

    for i in range(n):
        # print(i)
        if (s1[i] > s2[i]):
            return True
        elif (s1[i] < s2[i]):
            return False
        else:
            continue
    if len(s1) > len(s2):
        return True
    else:
        return False


s = input()
string = []
result = ""
num = len(s)
for i in range(num):
    string.append(s[i:])
# print(string)
for i in range(num - 1):
    for j in range(num - 1):
        if isCompare(string[j], string[j + 1]):
            t = string[j + 1]
            string[j + 1] = string[j];
            string[j] = t
for i in range(num):
    if i!=num-1:
        print(num + 1 - len(string[i]), end=" ")
    else:
        print(num+1 - len(string[i]))



