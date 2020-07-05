import string

dic = dict(zip(string.ascii_uppercase, [0] * 26))
s = input()
k = eval(input())
sz = len(s)
left = right = 0
curMax = 1
while right < sz:
    if s[right] == s[left]:
        dic[s[left]] += 1
        right += 1
        curMax = max(curMax, right - left)
    elif right - left < dic[s[left]] + k:
        right += 1
        curMax = max(curMax, right - left)
    else:
        dic[s[left]] -= 1
        left += 1
        if s[left - 1] != s[left]:
            right = left

print(curMax)
