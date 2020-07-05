# 利用并查集，相等的在一个并查集里
def is_avail(eqs):
    alphabet = {chr(i): chr(i) for i in range(97, 125)}

    def get_father(x):
        if x != alphabet[x]:
            alphabet[x] = get_father(alphabet[x])
        return alphabet[x]

    for eq in eqs:
        if eq[1] == '=':
            alphabet[get_father(eq[0])] = get_father(eq[-1])
            # 令其father相等

    for eq in eqs:
        if eq[1] == '!':
            if get_father(eq[0]) == get_father(eq[-1]):
                return "false"
    return "true"


def func():
    eqs = input()[2:-2].split("\",\"")
    print(is_avail(eqs))


func()
