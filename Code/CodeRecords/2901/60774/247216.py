def judge(s):
    if(len(s) == 1):
        return True
    else:
        temp = s[0]
        for i in range(1,len(s)):
            if(s[i] != temp):
                temp = s[i]
            else:
                return False
    return True

s = bin(int(input()))[2:]
print(judge(s))