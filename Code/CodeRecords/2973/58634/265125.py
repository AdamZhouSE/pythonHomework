def cal(str1,sub):
    res = 0
    l = list(sub)
    l.sort()
    substr = "".join(l)
    if len(str1)<8:
        return 0
    for i in range(0,len(str1)-7):
        temp = list(str1[i:i+8])
        temp.sort()
        temp = "".join(temp)
        if temp==substr:
            res+=1
    return res

ans = 0
str1 = input()
n = int(input())
for i in range(n):
    ans += cal(str1,input())
print(ans)