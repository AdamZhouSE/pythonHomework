num = int(input())
lists = []

for i in range(0, num):
    lists.append(int(input()))


def add(k, lists, count):
    if k == len(lists):
        if count == 0 or count%360==0:
            return True
        else:
            return False
    else:
        count = count + lists[k]
        A = add(k + 1, lists, count)
        count = count - 2 * lists[k]
        B = add(k + 1, lists, count)
        return A or B


if add(0, lists, 0):
    print("YES")
else:
    print("NO")
