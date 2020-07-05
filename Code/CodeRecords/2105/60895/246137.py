str=input().split(',')
str=list(map(int,str))
x1=str[2]-str[0]
y1=str[3]-str[1]
x2=str[6]-str[4]
y2=str[7]-str[5]
s1=x1*y1
s2=x2*y2
S=s1+s2
x=0
y=0
if str[4]>=str[2] or str[6]<=str[0] or str[1]>=str[7] or str[3]<=str[5]:
    S=S
elif str[4]<str[0]:
    if str[6]>=str[2]:
        x=str[2]-str[0]
    else:
        x=str[6]-str[0]
elif str[4]>=str[0]:
    if str[6]>=str[2]:
        x=str[2]-str[4]
    else:
        x=str[6]-str[4]
else:
    S=S
if str[4]>=str[2] or str[6]<=str[0] or str[1]>=str[7] or str[3]<=str[5]:
    S=S
elif str[5]<str[1]:
    if str[7]>=str[3]:
        y=str[3]-str[1]
    else:
        y=str[7]-str[1]
elif str[5]>=str[1]:
    if str[7]<str[3]:
        y=str[7]-str[5]
    else:
        y=str[3]-str[5]
else:
    S=S
s=x*y
S=S-s
print(S)