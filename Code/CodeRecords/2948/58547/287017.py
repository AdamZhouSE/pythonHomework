def add_neighbor(the_number_list):
    i = 0
    while i < len(the_number_list) - 1:
        the_number_list[i] = (str(
            (int(the_number_list[i]) + int(the_number_list[i + 1])) % 10
        ))
        i += 1
    the_number_list.pop()


def func():
    string = input()
    ST = int(input())
    the_number_list = list("".join([str(ord(x) - 65 + ST) for x in list(string)]))
    # print(the_number)

    while len(the_number_list) > 2:
        add_neighbor(the_number_list)
        # print(the_number_list)
        if the_number_list == list(str(100)):
            break

    print(int("".join(the_number_list)), end='', flush=True)


func()
