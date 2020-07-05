def getInput():
    input_str = input();
    nums_str = input_str[1:len(input_str) - 1];
    nums = [int(n) for n in nums_str.split(",")];
    return nums;

def getNum(l):
    m = max(l)

    tmp_list = []
    for i in range (m + 1):
        tmp_list.append(0)

    for i in range (len(l)):
        tmp_list[l[i]] += 1

    for i in range (len(tmp_list)):
        if tmp_list[i] == 1:
            return i

l = getInput()
p = getNum(l)
if p == None:
    print(l)
print(p)