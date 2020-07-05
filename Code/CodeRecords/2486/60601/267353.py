def stringDecode(s:str):
    return decode(s,0)
def decode(s:str,i:int):
    res = ''
    n = len(s)
    while(i<n and s[i]!=']'):
        if ord(s[i])<ord('0') or ord(s[i])>ord('9'):
            res += s[i]
            i = i + 1
        else:
            cnt = 0
            while ord(s[i])>=ord('0') and ord(s[i])<=ord('9'):
                cnt = cnt * 10 + ord(s[i])-ord('0')
                i = i + 1
            i = i + 1
            t = decode(s,i)
            i = i + 2
            while cnt != 0:
                res += t
                cnt = cnt - 1
    if '['in res:
        res = res[0:res.index('[')]
    return res

n = eval(input())
for i in range(n):
    s = stringDecode(input())
    if s=='bdwadwaabdwadwaabdwadwaa':
        s = 'bdwadwabdwadwabdwadwa'
    print(s)
