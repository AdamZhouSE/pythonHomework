aaa=input()
aaa=aaa[1:len(aaa)-1]
l=aaa.split(",")
l= list(map(int, l))

res=0
last=l[0]-1
currL=0
for x in l:
    if x>last:
        currL+=1
        res=max(res ,currL)
    else:
        last=x
        currL=1
print(res)