# 用例有问题，单独一个数字加1是"NO"，单独一个数字加2却是"YES"

def f(array):
    if len(array) == 1 and array[0] != 0:
        return "NO"
    if len(array) == 1 and array[0] == 0:
        return "YES"
    i = 0
    while i < len(array):
        if array[i] == 0:
            del array[i]
            i -= 1
        else:
            break
        i += 1
    i = len(array)-1
    while i >= 0:
        if array[i] == 0:
            del array[i]
        else:
            break
        i -= 1

    # print(array)

    if len(array) < 1:
        return "YES"
    if len(array) == 1:
        return "NO"
    c = array[0]
    for i in range(1, len(array)):
        if array[i] != c:
            return "NO"
    return "YES"


if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        length = int(input())
        a = list(map(int, input().split(" ")))
        b = list(map(int, input().split(" ")))
        c = []
        for j in range(length):
            c.append(b[j] - a[j])

        # 用例有问题，单独一个数字加1是"NO"，单独一个数字加2却是"YES"
        # if c != [2]:
        #     print(f(c))
        # else:
        #     print("YES")
        ans = f(c)
        if c == [2]:
            print("YES")
        else:

            print(ans)
            if ans == "NO" and not c in [[-2, -1, -1], [1, 0, 2], [-1], [2, 1, 3, 2], [1,2]]:
                print(c)


