def isValid(l):
    final_list = []
    final_list.append(max(l[0]))

    for i in range(1, len(l)):
        if max(l[i]) <= final_list[-1]:
            final_list.append(max(l[i]))
        elif min(l[i]) > final_list[-1]:
            print('NO')
            return False
        else:
            final_list.append(min(l[i]))
    print('YES')
    return True


def getInput():
    input_str = input();
    nums = [int(n) for n in input_str.split(" ")];
    return nums;


n = int(input())
l = []
for i in range (n):
    l.append(getInput())

isValid(l)