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
            if flag[0] == "true":
                break
            swap(index, start)
            if array[0]=="0":
                swap(index, start)
                continue
            func9(start + 1, end)
            swap(index, start)


string = input()
if string=="0":
    print("false")
else:
    array = list(string)
    n = len(array)
    flag = ["false"]
    func9(0, n)
    print(flag[0])