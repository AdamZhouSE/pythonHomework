def isEven(num):
    if num % 2 == 0:
        return True
    return False

def isOdd(num):
    if num % 2 == 0:
        return False
    return True

def getMax(l, flag):
    if flag == 'Even':
        for i in l:
            if isEven(i):
                return i
        return -1
    else:
        for i in l:
            if isOdd(i):
                return i
        return -1

def StartEven(l):
    l = sorted(l, reverse=True)
    pop_list = []
    flag = 0

    while len(l) != 0:
        if flag == 0:
            pop_num = getMax(l, 'Even')
            if pop_num == -1:
                break
            else:
                l.remove(pop_num)
                pop_list.append(pop_num)
                flag = 1
        else:
            pop_num = getMax(l, 'Odd')
            if pop_num == -1:
                break
            else:
                l.remove(pop_num)
                pop_list.append(pop_num)
                flag = 0
    # print(pop_list)
    return sum(l)

def StartOdd(l):
    l = sorted(l, reverse=True)
    pop_list = []
    flag = 0

    while len(l) != 0:
        if flag == 0:
            pop_num = getMax(l, 'Odd')
            if pop_num == -1:
                break
            else:
                l.remove(pop_num)
                pop_list.append(pop_num)
                flag = 1
        else:
            pop_num = getMax(l, 'Even')
            if pop_num == -1:
                break
            else:
                l.remove(pop_num)
                pop_list.append(pop_num)
                flag = 0
    # print(pop_list)
    return sum(l)

def getInput():
    input_str = input();
    nums = [int(n) for n in input_str.split(" ")];
    return nums;

input()
l = getInput()
print(min(StartEven(l), StartOdd(l)))
