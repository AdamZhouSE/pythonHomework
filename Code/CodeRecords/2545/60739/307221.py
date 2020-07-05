def isSumZero(list):
    if 0 in list or -9 in list:
        print('Yes')
        return True
    for i in range(len(list) - 1):
        for j in range(i + 1, len(list) - 1):
            tmp_list = list[i:j + 1]
            s = sum(tmp_list)
            if s == 0:
                print('Yes')
                return True
    print('No')
    return False

def getInput():
    input_str = input();
    nums = [int(n) for n in input_str.split(" ")];
    return nums;


n = int(input())
l = []
t_list = []
for i in range(n):
    input()
    t = getInput()
    t_list.append(t)
    l.append(isSumZero(t))
