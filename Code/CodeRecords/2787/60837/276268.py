def sort(List):
    for i in range(len(List)):
        for j in range(i + 1, len(List)):
            if List[i] > List[j]:
                temp = List[i]
                List[i] = List[j]
                List[j] = temp
    return List

def Sort(List):
    result=0
    for i in range(len(List)):
        result+=abs(List[i]-i-1)
    return result

n=int(input())
List=list(map(int,input().split(' ')))
List=sort(List)
print(Sort(List))