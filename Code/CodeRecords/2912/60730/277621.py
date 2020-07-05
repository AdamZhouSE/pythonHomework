s = input()
if s == "":
    print(0)
max_len = 0
cur_len = 0
left = 0
lookup = set()
n = len(s)
for i in range(n):
    cur_len += 1
    while s[i] in lookup:
        lookup.remove(s[left])
        left += 1
        cur_len -= 1
    if cur_len > max_len:
        max_len = cur_len
    lookup.add(s[i])
print(max_len)
