'''
题目描述:
给定一组非负整数，重新排列它们的顺序使之组成一个最大的整数。
'''

def sortedByFirstChar(arr,location):
    arr.sort(key=lambda x: x[location] , reverse=True)
    tempArr=[]
    special=-1
    for i in range(0,len(arr)-1):     # 如果第一位有重复的 按第二位排序 用递归
        try:
            if arr[i][location]==arr[i+1][location]:
                if i!=len(arr)-2:
                    tempArr.append(arr[i])
                else:
                    tempArr.append(arr[i])
                    tempArr.append(arr[i+1])

            else:
                if tempArr!=[]:   # 相同的暂时结束了
                    backArr = sortedByFirstChar(tempArr, location + 1)
                    # 往下继续比的时候 不带3
                    for k in range(len(backArr) - 1, -1, -1):  # 把3加上
                        if special[0] <= backArr[k][-1]:  # specil的第一个字符 必须<=他前面那个数的最后一个字符
                            newIndex = k + 1
                            break
                    backArr.insert(newIndex, special)

                    firstIndex = i - (len(backArr) - 1)
                    for k in range(0, len(backArr)):
                        arr[firstIndex + k] = backArr[k]
                    tempArr=[]
        except:   # 3 32 34这种的 3在比第二位的时候会报错 因为越界
            if len(arr[i])<len(arr[i+1]):
                tempArr.append(arr[i+1])
                special=arr[i]
            else:
                tempArr.append(arr[i])
                special=arr[i+1]
    if tempArr!=[]:
        strength=min(len(x) for x in tempArr)
        for item in tempArr:
            if len(item)==strength:
                special=item
                break
        tempArr.remove(special)
        backArr = sortedByFirstChar(tempArr, location + 1)
        for k in range(len(backArr) - 1, -1, -1):  # 把3加上
            if special[0] <= backArr[k][-1]:  # specil的第一个字符 必须<=他前面那个数的最后一个字符
                newIndex = k + 1
                break
        backArr.insert(newIndex, special)

        firstIndex = len(arr)-len(backArr)
        for k in range(0, len(backArr)):
            arr[firstIndex + k] = backArr[k]


    return arr

if __name__ == '__main__':
    arr=eval(input())
    arr = list(map(str, arr))
    arr=sortedByFirstChar(arr,0)
    result = ""
    for item in arr:
        result += item
    print(result)



