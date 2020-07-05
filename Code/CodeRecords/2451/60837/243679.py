def findPosition(List,x):
    for i in range(len(List)):
        if List[i]==x:
            return i
    for i in range(len(List)):
        if List[i]>x:
            return i
    return len(List)

List=list(map(int,input().split(',')))
x=int(input())
print(findPosition(List,x))