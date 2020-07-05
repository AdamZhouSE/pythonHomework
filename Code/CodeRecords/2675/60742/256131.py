t = int(input())
for k in range(t):
    n_str = input()
    n_new = []
    for i in range(len(n_str)):
        if n_str[i]=='6':
            n_new.append('9')
        else:
            n_new.append(n_str[i])
    n_new_int = int(''.join(n_new))
    n_int = int(n_str)
    print(n_new_int-n_int)