def func():
    start = list(input())
    end = list(input())

    if len(start) != len(end):
        print("False")
        return

    while "X" in start:
        start.remove("X")

    while "X" in end:
        end.remove("X")

    if start == end:
        print("True")
    else:
        print("False")


func()
