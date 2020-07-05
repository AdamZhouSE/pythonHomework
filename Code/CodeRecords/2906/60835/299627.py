n = int(input()) % 26
s = input()
res = list(s)
for x in range(len(res)):
    res[x] = chr(ord(res[x]) + n)
    #print(res[x])
print("".join(res), end = "")