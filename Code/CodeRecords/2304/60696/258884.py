n = 0
root = 0
lch = []
rch = []


def print_in_level():
    stack = [root]
    i = 0
    while len(stack) != 0:
        i += 1
        print('Level {:d} : '.format(i), end='')
        for each in stack[0:-1]:
            print(each, end=' ')
        print(stack[-1])
        temp = []
        for each in stack:
            if lch[each] != 0:
                temp.append(lch[each])
            if rch[each] != 0:
                temp.append(rch[each])
        stack = temp


def print_in_zigzag():
    stack = [root]
    i = 0
    while len(stack) != 0:
        i += 1
        if i%2 == 1:
            print('Level {:d} from left to right: '.format(i), end=' ')
            for each in stack[0:-1]:
                print(each, end=' ')
            print(stack[-1])
        else:
            print('Level {:d} from right to left: '.format(i), end=' ')
            for each in stack[::-1][0:-1]:
                print(each, end=' ')
            print(stack[0])
        temp = []
        for each in stack:
            if lch[each] != 0:
                temp.append(lch[each])
            if rch[each] != 0:
                temp.append(rch[each])
        stack = temp


if __name__ == '__main__':
    arr = [int(i) for i in input().split()]
    n = arr[0]
    root = arr[1]
    lch = [0 for i in range(500)]
    rch = [0 for i in range(500)]
    for i in range(n):
        arr = [int(j) for j in input().split()]
        lch[arr[0]] = arr[1]
        rch[arr[0]] = arr[2]
    print_in_level()
    print_in_zigzag()
