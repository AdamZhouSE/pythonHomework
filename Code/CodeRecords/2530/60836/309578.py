"""
字符串S和 T 只包含小写字符。在S中，所有字符只会出现一次
S 已经根据某种规则进行了排序。我们要根据S中的字符顺序对T进行排序。更具体地说，如果S中x在y之前出现，那么返回的字符串中x也应出现在y之前
返回任意一种符合条件的字符串T
"""

s=list(str(input()))
t=list(str(input()))

result=""

i=0
while(i<len(t)):
    if(s[i] in t):
        result+=s[i]
        del t[t.index(s[i])]
    i+=1

for i in range(len(t)):
    result+=t[i]

print(result)