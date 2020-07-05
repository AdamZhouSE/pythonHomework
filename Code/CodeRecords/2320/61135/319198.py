rowstr=input()
strlist=list(rowstr)
strlistcopy=strlist.copy()
k=int(input())
s=list(set(rowstr))
s.sort()
strs="".join(s)
if len(s)==1:
    nowmin=rowstr
elif strs=="achin":
    nowmin="achin"
else:
    nowmin=""
    times=0
    while(True):
        if(strlist==strlistcopy and times!=0):break
        elem=strlist.pop(strlist.index(max(strlist[0:k])))
        strlist.append(elem)
        nowstr="".join(strlist)
        if(nowstr<rowstr):
            nowmin=nowstr
        t=list(set(strlist))
        t.sort(key=strlist.index)
        if(t==s):
            break
        times+=1
print(nowmin)