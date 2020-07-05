s = input()
t = input()
list_s = list(s)
list_t = list(t)
Flag = True
for i in range(len(s)):
    if list_t.count(s[i]) > 0:
        list_t = list(t[list_t.index(s[i]) - i + 1:len(list_t) + 1])
    else:
        print(False)
        exit(-1)
if list_t.count(s[-1]) > 0:
    print(True)
else:
    print(False)