def func():
    n = int(input())
    bin_str = str(bin(n))
    if "00" not in bin_str and "11" not in bin_str:
        print("True")
    else:
        print("False")


func()
