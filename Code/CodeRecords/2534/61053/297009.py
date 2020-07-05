def add(candidate:list,newval:list):
    index = 0
    while index < len(candidate):
        if candidate[index][0] > newval[0]:
            break
        index += 1
    candidate.insert(index,newval)

def mergeArray(arrays:list):
    candidate = []
    indexs = []
    for i in range(len(arrays)):
        newval = []
        newval.append(arrays[i][0])
        newval.append(i)
        add(candidate,newval)
        indexs.append(0)

    res = []
    while candidate != []:
        res.append(candidate[0][0])
        indexOfArray = candidate[0][1]
        del candidate[0]
        indexs[indexOfArray] += 1
        if indexs[indexOfArray] != len(arrays[indexOfArray]):
            newval = [arrays[indexOfArray][indexs[indexOfArray]], indexOfArray]
            add(candidate,newval)
    return res

if __name__ == "__main__":
    arrays = eval(input())
    rse = mergeArray(arrays)
    print(rse)