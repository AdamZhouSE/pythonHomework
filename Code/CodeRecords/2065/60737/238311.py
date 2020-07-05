import re


def my_atoi(s):
    ret = re.findall(r"^[-+]?\d+", s.strip())
    if ret:
        ret_str = ret[0]
        ret_str2 = ''
        if ret_str[0] == '-' or ret_str[0] == '+':
            ret_str2 = ret_str[1:]
        else:
            ret_str2 = ret_str
        ret_int = int(ret_str2)
        if ret_str[0] == "-":
            return -ret_int if ret_int <= 2 ** 31 else -2 ** 31
        else:
            return ret_int if ret_int < 2 ** 31 else 2 ** 31 - 1
    else:
        return 0


if __name__ == "__main__":
    s = input()
    print(my_atoi(s))
