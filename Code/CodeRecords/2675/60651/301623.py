t=int(input())
for i in range(t):
    inlist=list(input())
    l=len(inlist)
    list1=[]
    list2=[]
    for i in range(l):
        if inlist[i]=="6":
            inlist[i]="9"
            list2=inlist.copy()
    for i in range(l):
        if inlist[i]=="9":
            inlist[i]="6"
            list1=inlist.copy()
    print(int("".join(list2))-int("".join(list1)))        
    