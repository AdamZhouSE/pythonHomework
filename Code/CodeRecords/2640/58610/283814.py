from pandas import value_counts
s = input()
t = input()
dict_t = dict(value_counts(list(t)))
required = len(dict_t)
left, right = 0, 0
formed = 0
windows_count = {}
ans = float('inf'), None, None

while right < len(s):
    char = s[right]
    windows_count[char] = windows_count.get(char, 0) + 1
    if char in dict_t and windows_count[char] == dict_t[char]:
        formed += 1
    while left <= right and formed == required:
        char = s[left]
        if right - left + 1 < ans[0]:
            ans = (right - left + 1, left, right)
        windows_count[char] -= 1
        if char in dict_t and windows_count[char] < dict_t[char]:
            formed -= 1
        left += 1
    right += 1
print("" if ans[0] == float('inf') else s[ans[1]:ans[2] + 1])