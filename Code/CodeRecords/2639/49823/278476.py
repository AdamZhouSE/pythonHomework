def bc(s,k):
    import collections
    r,n,l,mf=0,len(s),0,0
    d=collections.defaultdict(int)
    for r,c in enumerate(s):
        d[c]+=1
        mf=max(mf,d[c])
        while r-l+1-mf>k:
            d[s[l]]-=1
            l+=1
        r=max(r,r-l+1)
    print(r)
if __name__ == '__main__':
    bc(input(),int(input()))
