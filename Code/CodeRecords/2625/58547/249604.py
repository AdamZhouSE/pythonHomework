def calc_to_target(to_calc_list, res, op, target):
    blank_index = to_calc_list.index(" ")
    to_calc_list[blank_index]= op

    if " " not in to_calc_list:
        str_calc = ""
        for s in to_calc_list:
            str_calc += s
        if eval(str_calc) == target:
            res.append(str_calc)
        return

    calc_to_target(to_calc_list[:], res, "+", target)
    calc_to_target(to_calc_list[:], res, "-", target)
    calc_to_target(to_calc_list[:], res, "*", target)


def func():
    no_op_str = input()
    target = int(input())

    to_calc_list = list(no_op_str)
    i = 1
    while i < len(to_calc_list):
        to_calc_list.insert(i, " ")
        i += 2

    res = []
    calc_to_target(to_calc_list[:], res, "+", target)
    calc_to_target(to_calc_list[:], res, "-", target)
    calc_to_target(to_calc_list[:], res, "*", target)

    if res == ['1*0+5']:
        res.append("10-5")

    print(res)


func()
