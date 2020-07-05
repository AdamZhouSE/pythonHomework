tests = int(input())

for i in range(tests):
    boards = int(input())
    x = input()
    xlist = x.split(" ")
    lengthList = [int(xlist[i]) for i in range(len(xlist))]

    count = 0
    k = len(lengthList)
    while k > 0:
        for length in lengthList:
            if length >= k:
                count += 1
                
        if count >= k:
            print(k)
            break
        k -= 1
        count = 0

