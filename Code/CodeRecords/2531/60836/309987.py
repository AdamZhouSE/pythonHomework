"""
给定一个字符串，请将字符串里的字符按照出现的频率降序排列
"""

s=list(str(input()))

ch=[]
num=[]

while(len(s)>0):
    num.append(s.count(s[0]))
    ch.append(s[0])
    while(len(s)>0 and ch[len(ch)-1] in s):
        del s[s.index(ch[len(ch)-1])]

result=""
while(sum(num)>0):
    result+=ch[num.index(max(num))]*max(num)
    num[num.index(max(num))]=0

print(result)