def max_time():
    lst = list(input().split(','))
    lst.sort(reverse=True)
    for ch1 in lst:
        ans = ""
        if ch1 in '012':
            ans += ch1
            lst_c = lst.copy()
            lst_c.remove(ch1)
            for ch2 in lst_c:
                if '00' <= ch1 + ch2 <= '23':
                    ans += ch2
                    lst_c.remove(ch2)
                    ans += ':'
                    if '00' <= lst_c[0] + lst_c[1] <= '59':
                        ans += lst_c[0] + lst_c[1]
                        return ans
                    elif '00' <= lst_c[1] + lst_c[0] <= '59':
                        ans += lst_c[1] + lst_c[0]
                        return ans
    return ""


print(max_time())
