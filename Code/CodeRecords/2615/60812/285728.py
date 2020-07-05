T = int(input())
for i in range(T):
    s = ''.join(sorted(input(),reverse=True))
    n = len(s)
    if n <= 2:
        print(s)
    else:
        diff = ord(s[0]) - ord(s[1])
        length = maxlen = 2
        index = tempindex = 0
        for i in range(1, n - 1):
            tempdiff = ord(s[i]) - ord(s[i + 1])
            if tempdiff == diff:
                length += 1
            else:
                diff = tempdiff
                if length > maxlen:
                    maxlen = length
                    index = tempindex
                length = 2
                tempindex = i
        if length > maxlen:
            maxlen = length
            index = tempindex
        print(s[index:index+maxlen])