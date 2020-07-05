def compare(a):
    return a[0] / a[1]


def search(ls: list, target: int) -> list:
    res = []
    for i in range(len(ls)-1):
        for j in range(i+1, len(ls)):
            res.append([ls[i], ls[j]])
    res.sort(key=compare)
    return res[target-1]


lst = eval(input())
t = int(input())
print(search(lst, t))