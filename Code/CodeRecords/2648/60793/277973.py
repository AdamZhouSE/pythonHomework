def replace(s1: str, s2: str) -> str:
    '''if s1.find(s2) == -1:
        return s1
    else:'''
    temp = s1.find(s2)
    return s1[0: temp] + s1[temp + len(s2):]


str1 = input()
str2 = input()
while str1.find(str2) != -1:
    str1 = replace(str1, str2)
print(str1, end="")