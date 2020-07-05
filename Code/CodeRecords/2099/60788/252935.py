def f(a):
    s=0
    for i in list(a):
        s*=26
        s+=ord(i)-(ord('A')-1)
    return s

print(f(input().strip()))
    