def func27():
    n = eval(input())
    a = eval(input())
    b = eval(input())
    c = eval(input())
    val = 1
    while n > 0:
        if val % a == 0 or val % b == 0 or val % c == 0:
            n -= 1
        val += 1
    print(val - 1)


func27()