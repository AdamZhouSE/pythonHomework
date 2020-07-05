def getInput():
    input_str = input();
    nums = [int(n) for n in input_str.split(" ")];
    return nums;

def getNum(l):
    num1 = l.count(1)
    num2 = l.count(2)
    num3 = min(num1, num2)
    if num1 > num2:
        num3 += (num1 - num2) // 3
    return num3

input()
l = getInput()
p = getNum(l)
print(p)