a = input()
try:
    int(a)
    print(True)
except ValueError:
    try:
        float(a)
        print(True)
    except ValueError:
        print(False)