def isIsogram(s):
    for i in range(len(s)):
        if s.count(s[i]) != 1:
            return False
    return True


n = int(input())
string = []
for i in range(n):
    string.append(input())

for i in range(n):
    if isIsogram(string[i]):
        print(1)
    else:
        print(0)