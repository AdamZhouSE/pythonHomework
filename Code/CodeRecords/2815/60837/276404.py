def func(List):
    Not=0
    for i in range(len(List)):
        if List[i]<0:
            Not+=1
    count=0
    for i in range(len(List)):
        if List[i]==0:
            count+=1
        else:
            count+=abs(List[i])-1
    if Not%2!=0:
        count+=2
    return count

n=int(input())
List=list(map(int,input().split(' ')))
print(func(List))
            