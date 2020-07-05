string = input()
dic = eval(input())


def isvalid(s):
    ind = -1
    for ch in s:
        try:
            ind = string.index(ch, ind+1)
        except Exception:
            return False
    return True


ans = ''
for element in dic:
    if isvalid(element):
        if len(element) > len(ans):
            ans = element
        elif len(element) == len(ans):
            flag = False
            for i in range(0, len(element)):
                if ord(element[i]) < ord(ans[i]):
                    flag = True
                    break
            if flag:
                ans = element
print(ans)
