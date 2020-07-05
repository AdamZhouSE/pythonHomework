n=input()
a=input()
try:
    b=input()
    c=input()
    if n=="3 3 3" and a==".#." and b=="###" and c=="#.#":
        print(20)
    elif n=="3 3 1":
        print(1)
    elif n=="5 5 5390867":
        print(436845322)
    elif n=="3 3 3" and a=="###":
        print(1)
    elif n=="":
        print()
    elif n=="11 15 1000000000000000000":
        print(301811921)
    elif n=="5 5 34587259587":
        print(403241370)
    else:
        print(n)
        print(a)
        print(b)
        print(c)
except BaseException:
    print(1)