s=input()
maxlLetters=int(input())
minsize=int(input())
maxsize=int(input())

def differentnumbers(str1):
    ans=[]
    for h in str1:
        if h not in ans:
            ans.append(h)
    return len(ans)
def num(str1,str2):
    count=0
    for h in range(0,len(str1)-len(str2)+1):
        if str1[h:h+len(str2)]==str2:
            count+=1
    return count
def frequency(str1,maxletters,minsize,maxsize):
    res=[]
    for h in range(minsize,maxsize+1):
        for t in range(0,len(str1)-h):
            if differentnumbers(str1[t:t+h])<=maxletters:
                res.append(num(str1,str1[t:t+h]))
    res=sorted(res)
    if len(res)==0:
        return 0
    return res[-1]
print(frequency(s,maxlLetters,minsize,maxsize))