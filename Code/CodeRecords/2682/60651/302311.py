t=int(input())
for i in range(t):
    inlist=input().split()
    n=int(inlist[0])
    n1=int(inlist[1])
    n2=int(inlist[2])
    list1=list(bin(int(n)))

    l=len(list1)
    for i in range(n1,n2+1):
        if list1[l-i]=='0':
            list1[l-i]='1'
        elif list1[l-1]=='1':
            list1[l-i]='0'
    list1=[str(x) for x in list1]  

    print(int("".join(list1),2))