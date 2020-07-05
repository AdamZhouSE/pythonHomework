def check(s, k, t):
    s = s[1:len(s) - 1].split(",")
    for i in range(len(s)):
        for j in range(1,k + 1,1):
            if i + j < len(s):
                if abs(int(s[i + j]) - int(s[i])) <= t:
                    return True
            if i - j >= 0:
                if abs(int(s[i - j]) - int(s[i])) <= t:
                    return True

    return False


string = input()
# print(string)
i = string.split(", ")
# print(i[0])
# print(i[1])
# print(i[2])
s = i[0][7:]
n1 = int(i[1][4:])
n2 = int(i[2][4:])
# print(s)
# print(n1)
# print(n2)
if check(s, n1, n2):
    print("true")
else:
    print("false")