string = input()
all = []
for i in range(len(string)):
    all.append(string[i:])
all.sort()
s = ""
for i in all:
    s = s + (str(len(string)+1-len(i))+" ")
print(s[:-1])