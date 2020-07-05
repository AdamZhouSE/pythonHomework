def comp(str1,str2):
    if len(str1) != len(str2):
        return False
    else:
        if standard(str1) == standard(str2):
            return True
        else:
            return False

def standard(str):
    '''返回标准形式(排好序)'''
    lis = list(str)
    lis.sort()
    return ''.join(lis)

num = int(input())
words = [input() for i in range(num)]
all = []
for i in words:
    si = standard(i.strip())
    if si not in all:
        all.append(si)
print(len(all),end = '')
