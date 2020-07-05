def getTotalNumberOfSequences(m, n):
    if m < n:
        return 0

    if n == 0:
        return 1
    res = (getTotalNumberOfSequences(m - 1, n) +
           getTotalNumberOfSequences(m // 2, n - 1))
    return res 


def getInput():
    input_str = input();
    nums = [int(n) for n in input_str.split(" ")];
    return nums;

n = int(input())
for i in range(n):
    t = getInput()
    print(getTotalNumberOfSequences(t[0], t[1]))