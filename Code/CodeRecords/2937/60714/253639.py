temp = input()
diff = 0
for i in range(0, 16):
    if temp[i] != "CODEFESTIVAL2016"[i]:
        diff += 1
print(diff)