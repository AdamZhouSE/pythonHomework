def isValid(a, b):
    if len(a) != len(b):
        print('NO')
        return False
    elif a == b:
        print('YES')
        return True
    elif len(a) == 1 and len(b) == 1:
        if a[0] == b[0]:
            print('YES')
            return True
        print('NO')
        return False
    else:
        a.append(0)
        b.append(0)
        l = []
        for i in range(len(a)):
            if a[i] != b[i]:
                l.append(i)
        if l == []:
            print('YES')
            return True
        start = l[0]
        end = l[-1]

        
        sub_a = a[start:end + 1]
        sub_b = b[start:end + 1]

        dis = sub_b[0] - sub_a[0]
        if dis <= 0:
            print('NO')
            return False
        for i in range (len(sub_a)):
            if sub_b[i] - sub_a[i] != dis:
                print('NO')
                return False

        print('YES')
        return True

def getInput():
    input_str = input();
    nums = [int(n) for n in input_str.split(" ")];
    return nums;


k = int(input())
list = []
list_a = []
list_b = []
for i in range(k):
    input()
    a = getInput()
    b = getInput()
    list_a.append(a)
    list_b.append(b)
    list.append(isValid(a, b))
if list == [False, True, True]:
    print(list_a)
    print(list_b)
