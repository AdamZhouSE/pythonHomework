def findIncrease(list , index):
    length = 1
    for i in range(index + 1, len(list)):
        if list[i]>list[i-1]:
            length += 1
        else:
            return length
    return length

def question22():
    maxLen = 1
    num = int(input())
    array = list(map(int, input().split()))
    for i in range(0, num):
        length = findIncrease(list=array, index= i)
        maxLen = max(maxLen,length)
    return maxLen

if __name__ == '__main__':
    print(question22())