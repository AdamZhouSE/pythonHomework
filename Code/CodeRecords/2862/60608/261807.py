def func35():
    n = eval(input())
    arr = list(map(int, input().split()))
    even = []
    odd = []
    for i in arr:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    if len(even) == len(odd):
        print(0)
    elif len(even) > len(odd):
        while odd:
            even.remove(max(even))
            odd.remove(max(odd))
        even.remove(max(even))
        print(sum(even))
    else:
        while even:
            odd.remove(max(odd))
            even.remove(max(even))
        odd.remove(max(odd))
        print(sum(odd))


func35()
