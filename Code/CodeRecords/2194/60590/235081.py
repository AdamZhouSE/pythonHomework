tests = input()
tests = int(tests)

lists = []
for i in range(tests):
    list1 = list(map(int, input().split()))
    lists.append(list1)

def IsPrime(num):
    if num == 1:
        return False

    for i in range(2, num // 2 + 1):
        if num % i == 0:
            return False
    return True

def func(object):
    result = []
    for i in range(object[0], (object[1])+1):
        num = int(i)
        if IsPrime(num):
            result.append(num)
    for i in range(result.__len__()):
        if i == result.__len__()-1:
            print(str(result[i]), end="")
        else:
            print(str(result[i]) + " ", end="")
    print()

for i in range(lists.__len__()):
    func(lists[i])