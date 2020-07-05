def likely_to_trans(s1,s2):
    if len(s1)!=len(s2):return False
    Sum=0
    for i in range(len(s1)):
        if Sum>1:break
        if s1[i]!=s2[i]:Sum+=1
    else:
        if Sum==1:
            return True
    return False

def find_trans(prefix,s1,s2,l):
    if s2 not in l:return []
    if likely_to_trans(s1,s2):
        return [prefix+[s1,s2]]
    ans=[]
    if l:
        for i in l:
            if likely_to_trans(s1, i):
                new = l[:]
                new.remove(i)
                ans+=find_trans(prefix + [s1], i, s2, new)
    ans=list(filter(lambda x:x and x[-1]==s2,ans))
    if ans:
        ans.sort(key=lambda x: len(x))
        ans = list(filter(lambda x: len(x) == len(ans[0]), ans))
    return ans

s1=input()
s2=input()
l=eval(input())
ans=find_trans([],s1,s2,l)
print(ans)