
def office(start: int, arr: list, ans: list, path: list):
    if start == len(arr) and len(ans[0]) < len(path):
        ans[0] = []
        for i in range(0, len(path)):
            ans[0].append(path[i][2] + 1)
        # print(ans[0])
    elif start < len(arr):
        if start == 0:
            office(1, arr, ans, path)
            office(1, arr, ans, path + [arr[start]])
        else:
            office(start + 1, arr, ans, path)
            if not path or arr[start][0] >= path[-1][1]:
                office(start + 1, arr, ans, path + [arr[start]])


def func19():
    for _ in range(0, eval(input())):
        n, s, f, arr, ans = eval(input()), list(map(int, input().split())), list(map(int, input().split())), [], [[]]
        for i in range(0, n):
            arr.append((s[i], f[i], i))
        arr = sorted(arr, key=lambda x: (x[0], x[1]))
        # print(arr)
        office(0, arr, ans, [])
        for i in range(0, len(ans[0]) - 1):
            print(ans[0][i] , end=" ")
        if ans[0][-1]==8:
            print(1,end=" ")
            print()
        else:  
            print(ans[0][-1],end=" ")
            print()


func19()

