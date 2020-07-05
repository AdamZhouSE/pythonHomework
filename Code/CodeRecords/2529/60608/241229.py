def swap(a, b):
    tem = array[a]
    array[a] = array[b]
    array[b] = tem


def func9(start, end):
    if start == end:
        item = int("".join(array[:]))
        if item & (item - 1) == 0:
            flag[0] = "true"
    else:
        for index in range(start, end):
            swap(index, start)
            func9(start + 1, end)
            if flag[0] == "true":
                break
            swap(index, start)


string = input()
array = list(string)
n = len(array)
flag = ["false"]
func9(0, n)
print(flag[0])