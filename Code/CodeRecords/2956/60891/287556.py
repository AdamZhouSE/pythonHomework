def d(str1, str2, s1):
    s = str1 + str2
    if s1.find(s) == -1:
        return 1
    else:
        return 0


def dp(s_len, letter, s1):
    if s_len == 1:
        return 1
    else:
        ans_ = 0
        for i_ in range(26):
            ans_ += (dp(s_len - 1, letter_s[i_], s1) * d(letter_s[i_], letter, s1))
        return ans_


s2_len = int(input())
s1 = input()
letter_s = 'abcdefghijklmnopqrstuvwxyz'
ans = 0
for i in range(26):
    ans += dp(s2_len, letter_s[i], s1)
print(ans)
