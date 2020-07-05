def s13():
    num = list(eval(input()))
    dif = int(input())
    max_num = 1

    for i in range(len(num)):
        count = 1
        start = i
        while True:
            if start == len(num)-1:
                break
            try:
                j = num[start+1:].index(num[start] + dif) + start + 1
                start = j
                count = count + 1
                if count > max_num:
                    max_num = count
            except ValueError:
                break

    print(max_num)


s13()