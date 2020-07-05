n = int(input())


def get_bin(n=0):
    re_str = ""
    div = n
    rem = 0
    if n == 0:
        return "0"
    else:
        while div != 0:
            rem = div % 2
            div //= 2
            re_str += str(rem)
        return re_str[::-1]


def get_rev(s="1"):
    re_str = ""
    for i in range(len(s)):
        re_str += "1" if s[i] == "0" else "0"
    return re_str


def bin_to_int(s=''):
    res = 0
    for i in range(len(s)):
        if s[len(s) - 1 - i] == "1":
            res += 2 ** (len(s) - 1 - i)
    return res


print(bin_to_int(get_rev(get_bin(n))))