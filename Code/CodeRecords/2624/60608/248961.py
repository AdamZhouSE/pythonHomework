def compute(string):
    if string.isdigit():
        return [int(string)]
    else:
        res = []
        for i, item in enumerate(string):
            if item in ["+", "-", "*"]:
                arr1 = compute(string[0:i])
                arr2 = compute(string[i + 1:len(string)])
                for num1 in arr1:
                    for num2 in arr2:
                        if item == "+":
                            res.append(num1 + num2)
                        elif item == "-":
                            res.append(num1 - num2)
                        else:
                            res.append(num1 * num2)
    return res


def func23():
    string = input()
    arr = compute(string)
    print(arr)


func23()
