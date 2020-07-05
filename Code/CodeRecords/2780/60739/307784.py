def getRemain(list, n):
    total = 1
    for i in list:
        total = total * i
    return total % n

def getInput():
    input_str = input();
    nums = [int(n) for n in input_str.split(" ")];
    return nums;

n = int(input())
for i in range(n):
    input()
    l = getInput()
    k = int(input())
    print(getRemain(l, k))