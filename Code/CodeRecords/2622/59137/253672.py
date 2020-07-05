def s11():
    li = list(eval(input()))
    num = int(len(li) / 2)
    for x in li:
        if li.count(x) > num:
            print(x)
            return
    print("Error")


s11()