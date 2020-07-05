s = input()
if s == "25" * (len(s) // 2):
    print(1)
    exit()
cnt = 0
tmp = ""
for i in range(len(s)-1):
    if s[i] == "2":
        if s[i+1] != "5":
            continue
        else:
            tmp += "25"
    if tmp != "":
        cnt += 1
        tmp = ""
print(cnt)
