def judge(s):
    se=set(list(s))
    if len(se)==len(s):
        return False
    else:
        return True


x=int(input())
ans=0
if x<11:
    print(ans)
else:
    for i in range(11,x+1):
        if judge(str(i)):
            ans+=1
    print(ans)