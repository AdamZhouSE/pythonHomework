s = input()

res = []

def remove(s, ibegin, jbegin, tmp1, tmp2):
    left_p = 0
    right_p = 0
    for i in range(ibegin, len(s)):
        if s[i] == tmp1: left_p += 1
        if s[i] == tmp2: right_p += 1
        if left_p < right_p:
            for j in range(jbegin, i + 1):
                if s[j] == tmp2 and (j == jbegin or s[j - 1] != tmp2):
                    remove(s[:j] + s[j + 1:], i, j, tmp1, tmp2)
            return
    rev = s[::-1]
    if tmp1 == "(":
        remove(rev, 0, 0, ")", "(")
    else:
        res.append(rev)

remove(s, 0, 0, "(", ")")
res.reverse()
print(res)



    