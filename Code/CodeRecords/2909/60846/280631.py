import collections
def maxFreq(s,maxletters,minsize):
    n=len(s)
    d=collections.defaultdict(int)
    for i in range(n-minsize+1):
        tmp=s[i:i+minsize]
        if len(set(tmp))<=maxletters: d[tmp]+=1
    return max(d.values()) if d else 0
print(maxFreq(input(),int(input()),int(input())))