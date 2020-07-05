aaa=input()
aaa=aaa[1:len(aaa)-1]
l=aaa.split(",")
res=0
for i, j in l:
    print(i+j)