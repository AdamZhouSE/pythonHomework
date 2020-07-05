str = input().strip()
length = 1
for i in range(len(str)-1):
    s = set()
    j = i
    while j<len(str) and str[j] not in s:
        s.add(str[j])
        j += 1
    if j-i>length:
        length = j-i
print(length)