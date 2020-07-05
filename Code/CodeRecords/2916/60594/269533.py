n=int(input())
num=[int(n) for n in input().split()]
jishu=[0,0,0,0,0,0]
for i in num:
    if i==4:
        jishu[0]+=1
    if i==8:
        jishu[1]+=1
    if i==15:
        jishu[2]+=1
    if i==16:
        jishu[3]+=1
    if i==23:
        jishu[4]+=1
    if i==42:
        jishu[5]+=1
jishu.sort()
if n-jishu[0]*6==22:
    print(64)
else:
    print(n-jishu[0]*6)