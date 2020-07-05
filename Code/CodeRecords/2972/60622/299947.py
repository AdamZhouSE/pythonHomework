n=int(input())
for i in range(n):
    isOK=False
    s=list(input())
    t=list(input())
    if s==t:
        isOK=True
    else:
        if len(t)==len(s)+1 :
            index=-1
            for i in range(len(s)):
                if s[i] != t[i]:
                    index = i
                    break
            if index==-1 and s[-1]!=t[-1]:
                isOK=True
            else:
                tem=s[index-1]
                s.insert(index,t[index])
                if s==t and tem!=s[index]:
                    isOK=True
    if isOK:
        print("Yes")
    else:
        print("No")