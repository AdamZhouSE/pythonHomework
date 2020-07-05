numq=int(input())
for i in range(0,numq):
    tempstr=input()
    lenA=int(tempstr[0])
    lenB=int(tempstr[2])
    K=int(tempstr[4])
    listA=input().split(" ")
    listB=input().split(" ")
    for item in listB:
        listA.append(item)
    listA=sorted(listA)
    print(listA[K])