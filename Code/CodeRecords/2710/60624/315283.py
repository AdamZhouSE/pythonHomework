def func9():
    temp = list(map(int, input().strip().split(" ")))
    n = temp[0]
    q = temp[1]
    t = []
    while q > 0:
        q -= 1
        in_str = input().strip()
        if in_str[0] == "M":
            t.append(list(map(int, in_str[2:].split(" "))))
        else:
            question = list(map(int, in_str[2:].split(" ")))
            temp = []
            for i in t:
                if i[0] <= question[0] and i[1] >= question[1]:
                    temp.append(i[1])
            if len(temp) == 0:
                print(-1)
            else:
                print(min(temp))
    return
func9()