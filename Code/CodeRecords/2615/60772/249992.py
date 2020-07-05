
for _ in range(int(input())):
    string = input()
    string = list(set(string))
    string = sorted(string, reverse=True)
    m_min_string = ''
    for min_diff in range(12, 0, -1):
        min_string = ''
        for ele in string:
            ans = ele
            curr = ele
            while chr(ord(curr) - min_diff) in string:
                ans += chr(ord(curr) - min_diff)
                curr = chr(ord(curr) - min_diff)
            if len(ans) > len(min_string):
                min_string = ans
        if len(min_string) >= len(m_min_string):
            m_min_string = min_string
    print(m_min_string)