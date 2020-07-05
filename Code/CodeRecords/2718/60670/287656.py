def search(s):
    global ans
    if s>=ans:
        return
    ans=s
    global pairs
    for pair in pairs:
        slist=list(s)
        tmp=slist[pair[0]]
        slist[pair[0]]=slist[pair[1]]
        slist[pair[1]]=tmp
        search(''.join(slist))
s=input()
pairs=eval(input())
ans=s
for pair in pairs:
    slist=list(s)
    tmp=slist[pair[0]]
    slist[pair[0]]=slist[pair[1]]
    slist[pair[1]]=tmp
    search(''.join(slist))
print(ans)