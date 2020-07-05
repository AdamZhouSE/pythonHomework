def getInput():
    input_str = input();
    nums = [int(n) for n in input_str.split(" ")];
    return nums;

def getRightlist(l):
    s1 = l[::-1]
    new_numbers = []
    for x in s1:
        if x not in new_numbers:
            new_numbers.append(x)
    s2 = new_numbers[::-1]
    return s2

input()
l = getInput()
p = getRightlist(l)
print(len(p))
print(" ".join(str(i) for i in p))