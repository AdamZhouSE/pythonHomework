def isint(s):
    rs=False
    if s.isnumeric(): rs = True
    if s[0] == '-' or s[0] == '+' and s[1:].isnumeric(): rs = True
    return rs

def isfloat(s):
    rs=False
    aa=s.split('.')
    if len(aa)==2 and isint(aa[0]) and str(aa[1]).isnumeric():rs=True
    return rs

s=input()
rs=False
rs=isint(s)or isfloat(s)
ss=s.split('e')
if len(ss)==2 and (isint(ss[0])or isfloat(ss[0]))and isint(ss[1]):rs=True
print(rs)