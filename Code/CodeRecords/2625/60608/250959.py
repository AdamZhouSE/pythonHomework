def addOp(arr, expression, ans, num, target, res):
    if len(arr) == 0 and ans == target:
        res.append(expression)
    else:
        for i in range(1, len(arr) + 1):
            if i == 1 or arr[0] != "0":
                tem = int(arr[0:i])
                if expression == '':
                    addOp(arr[i:], arr[0:i], tem, tem, target, res)
                else:
                    addOp(arr[i:], expression + "+" + arr[0:i], ans + tem, tem, target, res)
                    addOp(arr[i:], expression + "-" + arr[0:i], ans - tem, -tem, target, res)
                    addOp(arr[i:], expression + "*" + arr[0:i], ans - num + num * tem, tem * num, target, res)


def func24():
    res = []
    addOp(input(), "", 0, 0, int(input()), res)
    print(res)


func24()