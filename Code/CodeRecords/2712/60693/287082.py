def getNext(s:str):
    sLen=len(s)
    next=[-1 for _ in range(sLen)]
    for i in range(1,sLen):
        j=next[i-1]  # j指代在0~i-1的子串中有最长相同前后缀的前缀最后的下标
        while s[j+1]!=s[i] and j>=0:
            j=next[j]
        if s[j+1]==s[i]:
            # 由于匹配到相同前后缀而跳出循环
            next[i]=j+1
        else:
            # 由于走到j==-1了而退出，没有相同前后缀
            next[i]=-1
    return next

def KMP(s1:str,s2:str):
    # 查找s2在s1中出现的次数,返回匹配次数
    next=getNext(s2)
    i,j,res=0,0,0
    s1Len,s2Len=len(s1),len(s2)
    while i<s1Len:
        if s1[i]==s2[j]:
            i+=1
            j+=1
            if j==s2Len:
                res+=1
                j=next[j-1]+1  # 此时s2的前j-1个字符应该和s1的从i之前的j个字符相等
        else:
            if j==0:
                # 从s2的第一位开始就不匹配
                i+=1
            else:
                j=next[j-1]+1
    return res

n=int(input())
S=[]
while n:
    showTimes={}
    for _ in range(n):
        inp=input()
        S.append(inp)
    T=input()
    for s in S:
        showTimes[s]=KMP(T,s)
    maxShowTimes=max(showTimes.values())
    print(maxShowTimes)
    for s in S:
        if showTimes[s]==maxShowTimes:
            print(s)
    n=int(input())