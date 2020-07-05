def getInput():
    input_str = input();
    nums = [int(n) for n in input_str.split(" ")];
    return nums;

def getMoney(l, n):
    m = max(l)
    total = m * n
    
    c = 0
    for i in range (n):
        c += l[i]
    return total - c

n = int(input())
l = getInput()
a = getMoney(l, n)
print(a)