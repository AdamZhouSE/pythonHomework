def is_palindromic(s):
    s1 = ""
    for ii in range(len(s)-1, -1, -1):
        s1 += s[ii]
    return s1 == s


n = int(input())
inp_str = []
for i in range(n):
    inp = input().split(" ")
    inp_str.append(inp[1])
new_str = []
for str1 in inp_str:
    for str2 in inp_str:
        new_str.append(str1+str2)
ans = 0
for st in new_str:
    if is_palindromic(st):
        ans += 1
print(ans)
