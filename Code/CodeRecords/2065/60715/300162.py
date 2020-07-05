def myAtoi( str):
    import re
    ret = re.findall(r"^[-+]?\d+", str.strip())
    if ret:
        ret_str = ret[0]
        ret_str2 = ""
        if ret_str[0] == "-" or ret_str[0] == "+":
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
s=input("")
print(myAtoi(s))