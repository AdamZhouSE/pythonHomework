s=input()
def do():
    global s
    from collections import Counter
    dic=dict(Counter(s))
    for key in dic:
        if dic[key]>(len(s)+1)//2:
            return ''
    cut=(len(s)+1)//2
    s=list(s)
    s.sort()
    ans=[None]*len(s)
    ans[::2]=s[:cut]
    ans[1::2]=s[cut:]
    return ''.join(ans)

print(do())