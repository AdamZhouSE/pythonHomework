aaa=input()
aaa=aaa[1:len(aaa)-1]
l=aaa.split(",")
res=0
for s1 in l:
    for s2 in l:
        for c1 in s1:
            print c1