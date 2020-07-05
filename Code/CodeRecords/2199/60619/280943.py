def get_pre(s1, s2):
    i = 0
    while i < min(len(s1), len(s2)):
        if s1[i] == s2[i]:
            i += 1
        else:
            break
    return s1[:i]


def get_longest_common(string):
    suffix = []
    for i in range(len(string)):
        suffix.append(string[i:])
    suffix.sort()
    longest = ""
    for k in range(len(suffix)-1):
        temp = get_pre(suffix[k], suffix[k+1])
        if len(temp) > len(longest):
            longest = temp
    if longest == "":
        return "$"
    return longest


origin = input()
result = 1
origin = get_longest_common(origin)
while origin != "$":
    result += 1
    origin = get_longest_common(origin)
print(result)