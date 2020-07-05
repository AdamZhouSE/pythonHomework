ts = int(input())
for t in range(ts):
    set_a = set(input())
    set_b = set(input())
    print(''.join(sorted(set_a ^ set_b)))
    print()
