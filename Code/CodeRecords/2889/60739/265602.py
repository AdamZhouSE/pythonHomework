def getInput():
    input_str = input();
    nums = [int(n) for n in input_str.split(" ")];
    return nums;

def getAverageVolume(l, n):
    total = 0
    for i in range (n):
        tmp = int(l[i])
        total += tmp
    return total

n = int(input())
l = getInput()
p = getAverageVolume(l, n)
a = p / n
a = format(a, '.6f')
print(a)