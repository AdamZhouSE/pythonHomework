s=list(input())
dic=dict()
for i in range(len(s)):
    dic.update({s[i]:i})
print(dic)