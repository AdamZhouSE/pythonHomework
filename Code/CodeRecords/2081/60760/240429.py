alist=input()
blist=input()
l=len(alist)
count=0
for i in range(0,l-len(blist)+1):
    if alist[0 :len(blist)]==blist:
        count=count+1
    alist=alist[1:len(alist)]
print(count,end="")