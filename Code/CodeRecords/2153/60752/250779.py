num=int(input())
rs=''
a=str(num)
negative=False
if num<0:
    negative=True
    rs='-'
    a=a[1:]
a=list(a)
a.reverse()
rs=rs+''.join(a)
if negative:
    while rs[1]=='0':
        rs=rs[0]+rs[2:]
else:
    while rs[0]=='0':
        rs=rs[1:]
print(rs)