T=int(input())
for i in range(T):
    tmp=""
    s=input()
    beg=0
    while beg<len(s)-1:
        pre = beg
        while s[beg]==s[beg+1]:
            pre=beg
            beg+=1
        beg+=1
        tmp+=s[pre]
    if s[-1]!=s[-2]:
        tmp+=s[-1]
    print(tmp)
#删除s中连续的重复数字
