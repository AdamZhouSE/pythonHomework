import functools
def cmp(a,b):
    if a + b > b + a:
        return -1
    else:
        return 1


a = [str(x) for x in eval(input())]
for i in sorted(a,key=functools.cmp_to_key(cmp)):
    print(i, end='')
print()


