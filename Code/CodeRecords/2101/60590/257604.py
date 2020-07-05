num = int(input())

def operater(num):
    s=str(num)
    res=0
    for i in range(len(s)):
        res+=int(s[i])*int(s[i])
    return res

def is_happyNum(num):
    for i in range(100):
        if(operater(num)==4):
            return False
        else:
            num=operater(num)
    return True

print(is_happyNum(num))