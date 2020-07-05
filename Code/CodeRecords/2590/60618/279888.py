t = int(input())
for k in range(0, t):
    name = list(input())
    less = list(set(name))
    re = ''

    for i in range(0, len(less)):
        if less[i] != 'a' and less[i] != 'e' and less[i] != 'i':
            if less[i] != 'o' and less[i] != 'u':
                if less[i] not in re:
                    re += less[i]

    if len(re) % 2 == 0:
        print("SHE!")
    else:
        print("HE!")
