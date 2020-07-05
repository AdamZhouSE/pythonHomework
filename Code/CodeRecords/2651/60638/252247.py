n=int(input())
for x in range(0,n):
    binary=bin(int(input()))
    listB=list(binary)
    if len(binary)%2==1:
        listB.insert(2,"0")
    for i in range(2,len(listB)):
        if i%2==0:
            temp=listB[i]
            listB[i]=listB[i+1]
            listB[i+1]=temp
    binary="".join(listB)
    print(int(binary,2))