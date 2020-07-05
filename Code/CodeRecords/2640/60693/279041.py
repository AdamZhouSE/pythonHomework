from collections import Counter
def minWindow(s,t):
    if not s or not t:
        return

    dictT=Counter(t)
    required=len(dictT)
    l,r=0,0
    uniqueCha=0
    windowChas={}
    # res of form(window length,left,right)
    res=float("inf"),None,None

    while r<len(s):
        tmpcha=s[r]
        windowChas[tmpcha]=windowChas.get(tmpcha,0)+1
        if tmpcha in dictT and windowChas[tmpcha]==dictT[tmpcha]:
            # only when the same character show the same times as the t ,uniquecha add 1
            uniqueCha+=1

        while l<=r and uniqueCha==required:
            # only when find a window that is required can add 1 to l
            tmpcha=s[l]

            if r-l+1<res[0]:
                res=(r-l+1,l,r)

            windowChas[tmpcha]-=1
            if tmpcha in dictT and windowChas[tmpcha]<dictT[tmpcha]:
                uniqueCha-=1

            l+=1
        r+=1

    return "" if res[0]==float("inf") else s[res[1]:res[2]+1]

s=input()
t=input()
print(minWindow(s,t))