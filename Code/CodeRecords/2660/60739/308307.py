def getPrint(l):
    current_str = ''
    for i in l:
        if i[0] == 'T':
            current_str += i[1]
        if i[0] == 'U':
            for j in range(int(i[1])):
                current_str = current_str[0:len(current_str) - 1]
        if i[0] == 'Q':
            print(current_str[int(i[1]) - 1])
    return current_str

def getInput():
    input_str = input();
    nums = [str(n) for n in input_str.split(" ")];
    return nums;

n = int(input())
l = []
for i in range(n):
    l.append(getInput())
getPrint(l)