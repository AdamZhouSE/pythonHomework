from functools import cmp_to_key
def custom_cmp(a,b):
    if a+b>b+a:
        return -1
    elif a+b<b+a:
        return 1
    else:
        return 0

t = int(input())
for i in range(t):
    n = int(input())
    li = input().split()
    li.sort(key=cmp_to_key(custom_cmp))
    print("".join(li))