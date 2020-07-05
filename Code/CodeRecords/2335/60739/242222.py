def getInput():
    x = int(input());
    y = int(input());
    list = []
    list.append(x)
    list.append(y)

    return list;

def getStep(x, y, step):

    if x > y:
        step += (x - y)
        return step
    elif step >= y:
        return 10000000
    elif x <= y/2:
        return getStep(x * 2, y, step + 1)
    elif x == y:
        return step
    else:
        a = getStep(x * 2, y, step + 1)
        b = getStep(x - 1, y, step + 1)
        return min(a,b)


if __name__ == '__main__':
    nums = getInput();
    step = 0
    a = getStep(nums[0], nums[1], step)
    print(a);


