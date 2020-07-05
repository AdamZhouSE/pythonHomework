def longest_subl(c, left_k, left_s):
    if len(left_s) == 0:
        return 0
    if left_s[0] != c:
        if left_k > 0:
            return 1 + longest_subl(c, left_k - 1, left_s[1:])
        return 0
    return 1 + longest_subl(c, left_k, left_s[1:])


string = input()
k = int(input())
max_l = 1
for i in range(len(string) - 1):
    ch = string[i]
    max_l = max(max_l, 1 + longest_subl(ch, k, string[i + 1:]))
print(max_l)
