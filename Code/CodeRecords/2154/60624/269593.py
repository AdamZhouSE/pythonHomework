def func27():
    n = input()
    size = len(n)
    if size == 1:
        print(True)
    elif size%2 == 0:
        print(n[:size//2][::-1] == n[size//2:])
    else:
        print(n[:size//2][::-1] == n[size//2+1:])

    return
func27()