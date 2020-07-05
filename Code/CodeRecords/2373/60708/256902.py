N=int(input())
for n in range(0,N):
    l=int(input())
    temp=input().split(" ")
    house=[]
    for item in temp:
        house.append(int(item))
    result1=0
    for i in range(0,len(house),2):
        result1=result1+house[i]
    result2=0
    for i in range(1,len(house),2):
        result2=result2+house[i]
    if(result1>result2):
        print(result1)
    else:
        print(result2)