
def comSort(List, result):
    if len(List)==0:
        return result
    newList = []
    for i in range(len(List)):
        if List[i] == 1:
            List[i] = 0
            for j in range(len(List)):
                List[j] -= 1
                if List[j] > 0:
                    newList.append(List[j])
            result += 1
            return comSort(newList, result)
    if len(newList)==0:
        return result
    newList[newList.index(min(newList))] = 0
    for i in range(len(newList)):
        newList[i] -= 1
    return comSort(newList, result+1)


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
print(comSort(com, 0))


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
print(comSort(com, 0))
