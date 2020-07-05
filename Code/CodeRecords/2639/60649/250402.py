import collections
s=input()
n=len(s)
k=int(input())
d=collections.defaultdict(int) #记录字符出现次数
start=0#左窗口
maxnum=0#记录该窗口中出现次数最多的字符
res=0
for i in range(n):
    d[s[i]]+=1
    maxnum=max(maxnum,d[s[i]])
    if i-start+1-maxnum>k:#修改K次已经不能使当前窗口全是相同字符
        d[s[start]]-=1
        maxnum=max(maxnum,d[s[i]])
        start+=1
    res=max(i-start+1,res)
print(res)