n=input()
numslist=input().split(" ")
numslist=list(int(a) for a in numslist)
numslist=set(numslist)
if(0 in numslist):
    numslist.remove(0)
print(len(numslist))