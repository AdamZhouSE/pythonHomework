numOfInput = int(input())
for i in range(numOfInput):
    numOfWindows = int(input())
    windows = input().split(" ")
    windows = list(map(int,windows))
    while len(windows)!=1:
        maxWindow = windows[0]
        for j in windows:
            if j > maxWindow:
                maxWindow = j
        print(maxWindow,end = " ")
        newWindows = []
        for j in range(len(windows)-1):
            if windows[j] > windows[j+1]:
                newWindows.append(windows[j+1])
            else:
                newWindows.append(windows[j])
        windows = newWindows
    print(windows[0])