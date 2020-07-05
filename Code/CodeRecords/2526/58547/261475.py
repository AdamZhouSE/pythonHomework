def func():

    arr0 = [int(x) for x in input()[1:-1].split(",") if x.isdigit()]
    arr1 = [int(x) for x in input()[1:-1].split(",") if x.isdigit()]
    print(sorted(arr0 + arr1))


func()
