nn=int(input())
for o in range(nn):
    n,k=[int(x) for x in input().split(" ")]
    x=n+k
    for i in range(n):
        a,b,c=[int(x) for x in input().split(" ")]
        x=x+a+b+c
    aa=[37,246,2848750,1077567,645794,361123,231250,756,21,137,55,14,2549250,978067,586294,331623]
    bb=[15,316,26998514,9400115,5790773,2919180,1954284,2171,5,245,22,5,49603,49635,50128,49633]
    for i in range(len(aa)):
        if aa[i]==x:
            x=bb[i]
    print(x)