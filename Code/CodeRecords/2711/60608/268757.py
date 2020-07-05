def sameSet(arr: list, word1: str):
    for array in arr:
        for word2 in array:
            tem = []
            for i in range(0, len(word1)):
                if word1[i] != word2[i]:
                    tem.append([word1[i], word2[i]])
            if len(tem) == 2 and tem[0][0] == tem[1][1] and tem[0][1] == tem[1][0]:
                return arr.index(array)
    return -1


def func11():
    arr = eval(input())
    ans = [[arr[0]]]
    for i in range(1, len(arr)):
        index = sameSet(ans, arr[i])
        if index < 0:
            ans.append([arr[i]])
        else:
            ans[index].append(arr[i])
    print(len(ans))


func11()
