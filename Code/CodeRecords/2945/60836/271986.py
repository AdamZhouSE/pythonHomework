"""
一个长度为 l(3≤l≤255) 的字符串中被反复贴有 boy 和 girl 两单词
后贴上的可能覆盖已贴上的单词（没有被覆盖的用句点表示）
最终每个单词至少有一个字符没有被覆盖。
问贴有几个 boy 几个 girl？
"""

s=list(str(input()))

boy=0
girl=0
m=0
b=False
o=False
y=False
g=False
i=False
r=False
l=False

while m<len(s):
    if s[m]=='b':
        b=True
        boy+=1
    elif s[m]=='o':
        o=True
        if not b:
            boy+=1
    elif s[m]=='y':
        if not o:
            boy+=1
        o = False
        b = False
    else:
        b = False;o = False;y = False

    if s[m]=='g':
        g=True
        girl+=1
    elif s[m]=='i':
        i=True
        if not g:
            girl+=1
    elif s[m]=='r':
        r=True
        if not i:
            girl+=1
    elif s[m]=='l':
        if not r:
            girl+=1
        g = False
        i = False
        r = False
        l = False
    else:
        g=False;i=False;r=False;l=False

    m+=1

print(boy)
print(girl,end='')