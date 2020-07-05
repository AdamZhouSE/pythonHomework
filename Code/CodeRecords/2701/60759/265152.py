def judge(lst):
    if lst[0][0] == lst[1][0] == lst[2][0] or lst[0][1] == lst[1][1] == lst[2][1]:
        return True
    lst.sort()
    if lst == [[0, 0], [1, 1], [2, 2]] or lst == [[0, 2], [1, 1], [2, 0]]:
        return True
    return False


records = eval(input())
a = [records[i] for i in range(len(records)) if i % 2 == 0]
b = [records[i] for i in range(len(records)) if i % 2]
if len(a) >= 3 and judge(a):
    print('A')
elif len(b) >= 3 and judge(b):
    print('B')
elif len(records) < 9:
    print('Pending')
else:
    print('Draw')
