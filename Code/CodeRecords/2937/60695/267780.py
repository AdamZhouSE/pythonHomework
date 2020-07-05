s = input()
string = "CODEFESTIVAL2016"
count = 0
i = 0
for i in range(0, 16):
    if s[i] != string[i]:
        count += 1
print(count)