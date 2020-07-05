def makestr(s,index):
    resstr=[]
    if index== 0:
        resstr=list(s)
        resstr[0]='{'
        return ''.join(resstr)
    elif index== -1:
        resstr=list(s)
        resstr[-1]='}'
        return ''.join(resstr)
    else:
        return EOFError;
def isok(s):
    global res
    if s[0] != '{':
        s = makestr(s,0)
        res += 1
    if s[-1] != '}':
        s = makestr(s, -1)
        res += 1
    if ismatch(s):
        return
    else:
        isok(s[1:-1])

def ismatch(s):
    stack = []
    if s[0] == '}' or s[-1]=='{':
        return False
    for i in s:
        if i == '}' and len(stack)>0:
            stack.pop()
        elif i == '{':
            stack.append(i)
        else:
            return False
    if len(stack) == 0:
        return True
    return False

if __name__=="__main__":
    t=int(input())
    for te in range(t):
        s = input()
        res = 0
        if len(s) % 2 != 0:
            print(-1)
        else:
            isok(s)
            if res==4:
                res=2
            print(res)