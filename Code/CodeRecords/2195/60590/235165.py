tests = input()
tests = int(tests)

lists = []
for i in range(tests):
    list1 = list(map(int, input().split()))
    lists.append(list1)

def ones(str):
    ones=0
    lists = list(str)
    for i in range(lists.__len__()):
        if lists[i] == '1':
            ones += 1
    return ones

def IsPrime(num):
    if num == 1:
        return False

    for i in range(2, num // 2 + 1):
        if num % i == 0:
            return False
    return True


def func(object):
    result = []
    for i in range(object[0], object[1]+1):
        num = int(i)
        str = bin(num)
        numOfones = ones(str)
        numOfones = int(numOfones)
        if IsPrime(numOfones):
            result.append(num)
    print(result.__len__())

for i in range(lists.__len__()):
    func(lists[i])