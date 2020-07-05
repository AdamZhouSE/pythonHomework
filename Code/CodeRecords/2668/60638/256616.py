n=int(input())
for x in range(0,n):
    num=int(input())
    binaryN=list(bin(num))
    for i in range(2,len(binaryN)):
        if binaryN[i]=="1":
            binaryN[i]="0"
        else:
            binaryN[i]="1"
    numR=int("".join(binaryN),2)
    print(numR,end=" ")
    print(numR+num)