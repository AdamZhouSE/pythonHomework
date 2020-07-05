def func1():
    string = input()
    n = len(string)
    for i in range(n - 1, -1, -1):
        string += string[i]
    print(string)

func1()
