def isRev(string):
    if string == string[::-1]:
        return True
    return False


string = input()
orderNums = int(input())

for i in range(orderNums):
    order = input().split()
    if order[0] == '1':
        string += order[1]
    elif order[0] == '2':
        string = order[1][::-1] + string
    else:
        count = 0
        for length in range(1, len(string) + 1):
            for startPosition in range(0, len(string) - length + 1):
                substring = string[startPosition: startPosition + length]
                if isRev(substring):
                    count += 1
        print(count)