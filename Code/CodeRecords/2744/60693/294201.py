def findInSame(ws:[str]):
    # 同寄或同偶的不同字符串的连接，只有两个都是由单个相同字符组合成的才可以
    m=len(ws)
    res=0
    for i in range(m-1):
        for j in range(i+1,m):
            if set(ws[i])==set(ws[j]) and len(set(ws[i]))==1:
                res+=2
    return res

def findInDiff(ws0:[str],ws1:[str]):
    # 一奇一偶的不同字符串组合，当且仅当偶字符串长度是寄字符串长度两倍且有公共，或者两个都是同单个字符组成
    len0,len1=len(ws0),len(ws1)
    res=0
    for s0 in ws0:
        for s1 in ws1:
            if set(s0)==set(s1) and len(set(s1))==1:
                res+=2
            elif len(s0)==2*len(s1) and s1==s0[:len(s1)]:
                res+=2
    return res


from collections import defaultdict
words=defaultdict(list)
n=int(input())
for _ in range(n):
    inp=input().split()
    wordlen=int(inp[0])%2
    words[wordlen].append(inp[1])
# print(words)
res=0
res+=n
res+=findInSame(words[0])
# print(res)
res+=findInSame(words[1])
# print(res)
res+=findInDiff(words[0],words[1])
# print(res)
print(res)