def s4():
    array = list(eval(input()))
    blocks = []

    def find_num(x):
        for block in blocks:
            for i in block:
                if i == x:
                    return True
        return False

    for n in range(len(array)):
        next = array[n]
        block = []
        while not find_num(next) and next not in block:
            block.append(next)
            next = array[next]
        if len(block) != 0:
            block = list(set(block))
            blocks.append(block)

    count = 0
    nums = []
    for block in blocks:
        if len(block) != 1:
            max0 = max(block)
            min0 = min(block)
            flag = False
            for i in range(min0, max0+1):
                if i not in nums:
                    nums.append(i)
                    flag = True
            if flag:
                count = count + 1
    for block in blocks:
        if len(block) == 1 and block[0] not in nums:
            nums.append(block[0])
            count = count + 1
    print(count)
    
    
s4()