def findKmin(List, k):
    contrast = []
    for i in range(len(List)):
        for j in range(i + 1, len(List)):
            contrast.append(List[i] / List[j])
    target = findmin(contrast, k)
    for i in range(len(List)):
        for j in range(i + 1, len(List)):
            if List[i] / List[j] == target:
                return ([List[i], List[j]])


def findmin(List, k):
    result = []
    for i in range(len(List)):
        result.append(min(List))
        List.remove(min(List))
        if len(result) == k:
            return result[k - 1]


str=input()
List=[]
for i in range(len(str)):
    if str[i].isdigit():
        List.append(int(str[i]))
k = int(input())
print(findKmin(List, k))