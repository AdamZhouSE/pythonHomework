nfq=int(input())

list1=[]
list2=[]
check=["Yes"]*nfq
for i in range(0,nfq):
    temp=input()
    list1.append(input().split(" "))
    list2.append(input().split(" "))
for i in range(0,nfq):
    listbig=list1[i]
    listsmall=list2[i]
    for item in listsmall:
        if not item in listbig:
            check[i]="No"
for item in check:
    print(item)