aaa=input()
aaa=aaa[1:len(aaa)-1]
l=aaa.split(",")
res=0
for s1 in l:
    for s2 in l:
        flag=0
        for c1 in s1:
            if c1 in s2[1:len(s2)-1]:
                flag=1
                break
        if(flag==0):
            res=max(res, (len(s1)-2)*(len(s2)-2))
print(res)