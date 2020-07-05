def isok(s):
    global res
    if len(s)==0:
        return
    if s[0]=='{' and s[-1]=='}':
        isok(s[1:-2])
    else:
        if s[0]!='{':
            res+=1
        if s[-1]!='}':
            res+=1
        isok(s[1:-2])
        
t=int(input())
for test in range(t):
    s = input()
    res=0
    if len(s)%2!=0:
        print(-1)
    else:
        isok(s)
        print(res)
        