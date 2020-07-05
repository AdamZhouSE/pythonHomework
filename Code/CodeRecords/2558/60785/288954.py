"""
}{{}}{{{            3
{{}}}}              1
{{}{{{}{{}}{{       -1
{{{{}}}}            0
"""
def isok(s):
    global res
    if len(s) == 0:
        return
    if s[0] == '{' and s[-1] == '}':
        if len(s) == 2:
            return
        isok(s[1:-1])
    else:
        if s[0] != '{':
            res += 1
        if s[-1] != '}':
            res += 1
        isok(s[1:-1])

if __name__=="__main__":
    t=int(input())
    for te in range(t):
        s = input()
        res = 0
        if len(s) % 2 != 0:
            print(-1)
        else:
            isok(s)
            print(res)
    



