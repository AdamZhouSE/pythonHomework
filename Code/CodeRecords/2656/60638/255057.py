n=int(input())
for x in range(0,n):
    list1=list(map(int,input().split(" ")))
    bin1=bin(list1[0])
    bin2=bin(list1[1])
    if len(bin2)<len(bin1):
        listb=list(bin2)
        listb.insert(2,"0"*(len(bin1)-len(bin2)))
        bin2="".join(listb)

    if len(bin1)<len(bin2):
        listb = list(bin1)
        listb.insert(2, "0" * (len(bin2) - len(bin1)))
        bin1 = "".join(listb)
    i=1
    for i in range(1,len(bin1)):
        if bin1[0-i]!=bin2[0-i]:
            break
    print(i)