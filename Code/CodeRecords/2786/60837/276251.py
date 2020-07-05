def comSort(List):
    if len(List)==0:
        return 0
    newList=[]
    List[List.index(min(List))]=0
    for i in range(len(List)):
        List[i]-=1
        if List[i]>0:
            newList.append(List[i])
    return 1+comSort(newList)


def sort(List):
    for i in range(len(List)):
        for j in range(i + 1, len(List)):
            if List[i] > List[j]:
                temp = List[i]
                List[i] = List[j]
                List[j] = temp
    return List



def sort(List):
    for i in range(len(List)):
        for j in range(i + 1, len(List)):
            if List[i] > List[j]:
                temp = List[i]
                List[i] = List[j]
                List[j] = temp
    return List


n = int(input())
com = list(map(int, input().split(' ')))
com = sort(com)
print(comSort(com))
