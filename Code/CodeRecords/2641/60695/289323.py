a = input()
b = input()
s = "abcdefghijklmnopqrstuvwxyz"
dicta = {}
dictb = {}
flag = False
for i in range(0, 26):
    dicta[s[i]] = 0
    dictb[s[i]] = 0
for i in range(0, len(a)):
    dicta[a[i]] += 1
    dictb[b[i]] += 1
if dicta == dictb:
    print("True")
else:
    for i in range(0, len(b)-len(a)):
        dictb[b[i]] -= 1
        dictb[b[i+len(a)]] += 1
        if dicta == dictb:
            flag = True
            break
print(flag)
