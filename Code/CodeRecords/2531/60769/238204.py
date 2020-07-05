str1 = list(input())
dict = {}
for ch in str1:
    if ch in dict:
        dict[ch] += 1
    else:
        dict[ch] = 1
dict = sorted(dict.items(), key=lambda x: x[1], reverse=True)
res = ""
for item in dict:
    for i in range(item[1]):
        res+=item[0]
print(res)
