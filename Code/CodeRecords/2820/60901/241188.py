def question5():
    numOfCos = int(input())
    timeList = {}
    for i in range(0, numOfCos):
        time = input()
        if not timeList.__contains__(time):
            timeList[time] = 1
        else:
            timeList[time] += 1
    max = 0
    for value in timeList.values():
        if value > max:
            max = value
    return max

if __name__ == '__main__':
    print(question5())