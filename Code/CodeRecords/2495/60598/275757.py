string = input()
directory = input()[1:-1].split(",")
strings = [s[1:-1] for s in directory]
# print(strings)
store = [0 for i in range(26)]
for k in range(len(string)):
    store[ord(string[k])-ord("a")] += 1


def sub(temp):
    Tstore = [0 for i in range(26)]
    for i in range(len(temp)):
        Tstore[ord(temp[i])-ord("a")] += 1
    for j in range(26):
        if store[j] < Tstore[j]:
            return False
    return True


result = ""
L = 0
for s in strings:
    if sub(s):
        if len(s) > L:
            result = s
            L = len(s)
        elif len(s) == L:
            if s < result:
                result = s
print(result)
