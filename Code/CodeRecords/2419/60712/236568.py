n = input()
res1 = 1
res2 = 0
for i in range(len(n)):
    res1 = res1*int(n[i:i+1])
    res2 = res2+int(n[i:i+1])
print(res1-res2)