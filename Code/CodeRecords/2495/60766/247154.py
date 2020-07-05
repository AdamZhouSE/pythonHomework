def contens(a, s):
    for i in range(len(a)):
        if a[i] in s:
            return contens(a[i+1:], s[s.index(a[i])+1:])
        else:
            return False
    return True

def funct(res, p):
    if len(p)>len(res):
        return p
    return res

s=input()
dic=eval(input())
res=''
for i in range(len(dic)):
    if contens(dic[i], s):
        res=funct(res, dic[i])
print(res)