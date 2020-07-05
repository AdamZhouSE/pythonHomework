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
    base = object[0] + object[1]
    temp = object[0] + object[1]
    temp = int(temp)
    while not IsPrime(temp+1):
        temp += 1
    print(temp+1-base)

for i in range(lists.__len__()):
    func(lists[i])