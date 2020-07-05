# 思想就是：类似于字典排序
# 每个数，最左边的数大的往前排
# 最左边的数一样的话，看最右边的数字，最右边的数字大的在前面
# 如果这个数只有一位，最左边和最右边的数一样
# 3 31 34的排序就是 34 3 31

# 具体实现：
# 用三个数组，一个保存源数字，一个保存最左边的数，一个保存最右边的数
outcome = ''

length = int(input())
numlist = input().split(" ")
head = []
tail = []

for i in numlist:
    head.append(int(i[0]))
    tail.append(int(i[-1]))


# 首先对这三个数组按照最左边的数从大到小排序

def findMax():
    # 用于寻找一个数组里面最大的数的位置
    maxPosition = 0
    for i in range(0, len(head)):
        if head[i] > head[maxPosition]:
            maxPosition = i
    return maxPosition


headlistSorted = []
taillistSorted = []
numlistSorted = []

for i in range(0, length):
    maxPosition = findMax()
    headlistSorted.append(head[maxPosition])
    taillistSorted.append(tail[maxPosition])
    numlistSorted.append(numlist[maxPosition])
    head.remove(head[maxPosition])
    tail.remove(tail[maxPosition])
    numlist.remove(numlist[maxPosition])


# 排序完毕
def isSingle(i):
    i = int(i)
    string = ''
    for j in headlistSorted:
        string = string + str(j)
    l_index = string.index(string[i])
    r_index = string.rindex(string[i])
    if l_index == r_index:
        return True
    return False


for i in range(0, length):
    index = 0
    if len(headlistSorted) == 0:
        break
    # 首先是独个最大数
    if isSingle(index):
        outcome = outcome + numlistSorted[index]
        numlistSorted.remove(numlistSorted[index])
        headlistSorted.remove(headlistSorted[index])
        taillistSorted.remove(taillistSorted[index])
        continue

    # 不是独个最大数
    def findLastSamePosition():
        position = 0
        if len(headlistSorted) == 1:
            return 0
        for i in range(1,len(headlistSorted)):
            if headlistSorted[position] != headlistSorted[i] :
                return i-1
            return len(headlistSorted) - 1


    end = findLastSamePosition()


    def findinSameMax(end):
        end = int(end)
        positionMax = 0
        for i in range(0, end+1):
            if taillistSorted[positionMax] < taillistSorted[i]:
                positionMax = i
        return positionMax

    position = findinSameMax(end)
    outcome = outcome + numlistSorted[position]
    del numlistSorted[position]
    del headlistSorted[position]
    del taillistSorted[position]
print(outcome)