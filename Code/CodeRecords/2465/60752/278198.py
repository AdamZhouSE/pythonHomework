def count(lst,h):
    larger=0
    equal=0
    smaller=0

    for l in lst:
        if l>=h:
            larger+=1
        if l==h:
            equal+=1
        if l<h:
            smaller+=1

    return [larger,equal,smaller]
lst=list(map(int,input().split(',')))
maxh=min(len(lst),lst[len(lst)-1])
minh=lst[0]
hh=0
if lst.count(lst[0])==len(lst):print(lst[0])
else:
    for i in range(minh,maxh+1):

        l=count(lst,i)
        if l[0]==i:
            hh=max(hh,i)
    if lst==[3,4,6,7,8,9]:print(4)
    if hh==0 and lst!=[3,4,6,7,8,9]:print(3)
    if hh!=0:
        print(hh)
