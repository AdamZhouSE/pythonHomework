def func():
    target = input()
    try:
        while True:
            string = input()
            string = string.replace(target.upper(), "")
            string = string.replace(target.lower(), "")
            string = string.replace(" ", "")
            print(string)
    except EOFError:
        return


func()
