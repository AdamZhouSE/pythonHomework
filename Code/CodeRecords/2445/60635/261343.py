info=input().replace(' ','').split(',')
s=None
t=None
exec (info[0])
exec (info[1])
def judge(s,t):
    if len(s)==len(t):
        for a in s:
            if a not in t:
                return False
        return True
    return False
if judge(s,t):
    print('true')
else:
    print('false')