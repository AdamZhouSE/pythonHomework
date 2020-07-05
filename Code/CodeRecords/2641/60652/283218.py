def make_dict(s):
    d={}
    for i in s:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    return d
def contain_str():
    s1=input()
    s2=input()
    length=len(s1)
    l,r=0,length
    d1=make_dict(s1)
    while r<=len(s2):
        d2=make_dict(s2[l:r])
        if d1==d2:
            return True
        l+=1
        r+=1
    return False
print(contain_str())