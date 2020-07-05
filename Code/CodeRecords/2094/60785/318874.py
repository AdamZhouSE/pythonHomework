def isNumber( s):
    def isInt(s):
        NO_NUM = True
        for i in range(len(s)):
            if s[i] == "+" or s[i] == "-":
                if i == 0:
                    continue
                else:
                    return False
            elif s[i] in "1234567890":
                NO_NUM = False
            else:
                return False
        return not NO_NUM
    def isFloat(s):
        DOT_COUNT = 0
        NO_NUM = True
        for i in range(len(s)):
            if s[i] == "+" or s[i] == "-":
                if i == 0:
                    continue
                else:
                    return False
            elif s[i] == ".":
                DOT_COUNT += 1
                if DOT_COUNT > 1:
                    return False
            elif s[i] in "1234567890":
                NO_NUM = False
            else:
                return False
        return not NO_NUM