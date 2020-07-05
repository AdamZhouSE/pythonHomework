string = input()
k = int(input())
l, r = 0, 0
cs = [0 for i in range(26)]
for r in range(len(string)):
    cs[ord(string[r]) - ord('A')] += 1
    max_cl = max(cs)
    if r - l + 1 > max_cl + k:
        l += 1
        cs[ord(string[l]) - ord('A')] -= 1
print(r - l + 1)
