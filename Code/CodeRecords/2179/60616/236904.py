inp1=input().split()
leng=inp1[0]
num=int(inp1[1])
s=input()

for n in range (num):
    inps=input().split()
    a=int(inps[0])
    b=int(inps[1])
    c=int(inps[2])
    d=int(inps[3])
    tmpSubs=[]
    subs=[]
    count=0
    for i in range(a):
        for j in range(i, b):
            tmpSubs.append(s[i:j])
    tmpDic = {}
    for tmpSub in tmpSubs:
        tmpDic[tmpSub] = tmpSubs.count(tmpSub)
    for key, value in tmpDic.items():
        subs.append(key)
        count=count+1
    subs.remove('')
    comp = []
    comp.append(s[c:d])
    lens = []
    for sub in subs:
        comp.append(sub)
        s1 = min(comp)
        s2 = max(comp)
        for i, c in enumerate(s1):
            if c != s2[i]:
                pref = s1[:i]
                break
        pref = s1
        lens.append(len(pref))
    if(lens==[]):
        print(1)
    else:
        print(int(max(lens))+1)