def calc_max_split(number):
    if number <= 4:
        return number

    return max(
        number,
        sum([
            calc_max_split(number // 2),
            calc_max_split(number // 3),
            calc_max_split(number // 4)
        ])
    )


def func():
    test_num = int(input())
    i = 0
    while i < test_num:
        number = int(input())
        print(max(number, calc_max_split(number)))
        i += 1


func()
