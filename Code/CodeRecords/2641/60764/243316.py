s1=input()
s2=input()
ls1=list(s1)
ls1.sort()
res=False
start,end=0,len(s1)-1
while end<len(s2):
    tem=list(s2[start:end+1])
    tem.sort()
    if tem==ls1:
        res=True
        break
    start+=1
    end+=1
print(res)