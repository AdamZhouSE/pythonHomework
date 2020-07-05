def lengthOfLongestSubstring(s):
    if s == '':
        return 0
    if len(s) == 1:
        return 1

    def find_left(s, i):
        tmp_str = s[i]
        j = i - 1
        while j >= 0 and s[j] not in tmp_str:
            tmp_str += s[j]
            j -= 1
        return len(tmp_str)

    length = 0
    for i in range(0, len(s)):
        length = max(length, find_left(s, i))
    return length

s=input()
print(lengthOfLongestSubstring(s))