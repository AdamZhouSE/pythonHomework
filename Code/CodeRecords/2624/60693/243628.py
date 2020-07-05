def diff_compute(s):
    res=[]
    if len(s)==0:
        return res
    flag=False
    for i in range(len(s)):
        if s[i].isdigit():continue
        flag=True
        lres=diff_compute(s[:i])
        rres=diff_compute(s[i+1:])
        for n in lres:
            for m in rres:
              if s[i]=='+':res.append(int(n)+int(m))
              elif s[i]=='-':res.append(int(n)-int(m))
              elif s[i]=='*':res.append(int(n)*int(m))
    if not flag:res.append(s)
    return res

expre=input()
print(diff_compute(expre))