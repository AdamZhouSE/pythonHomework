def question25():
    num = int(input())
    l = list(map(int, input().split()))
    maxNum = max(l)
    minNum = min(l)
    maxIndex = 0
    minIndex = 0
    for i in range(num):
        if l[i] == maxNum:
            maxIndex = i
        elif l[i] == minNum:
            minIndex = i
    return max(abs(num - 1 - minIndex),abs(num - 1 - maxIndex),maxIndex,minIndex)

if __name__ == '__main__':
    print(question25())