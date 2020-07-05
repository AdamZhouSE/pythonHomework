

def print_stars(n):
    i = 0
    while i < n:
        print("*", end="", flush=True)
        i += 1


def print_ds(n):
    i = 0
    while i < n:
        print("D", end="", flush=True)
        i += 1


def print_diamond():
    n = int(input())
    arr = [1] * n
    i = int((n - 1) / 2)
    counter = 0
    while i >= 0:
        arr[counter] = i
        arr[n - counter - 1] = i
        i -= 1
        counter += 1
    for num in arr:
        print_stars(num)
        print_ds(n - 2 * num)
        print_stars(num)
        print()


print_diamond()
