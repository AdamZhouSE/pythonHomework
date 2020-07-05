def f(li1, li2):
    for i in li1:
        if i not in li2:
            return True
    return False


cars = int(input())
i = list(map(int, input().split(" ")))
o = list(map(int, input().split(" ")))
count = 0
for q in range(0, cars-1):
    current = o[q]
    origin_index = i.index(current)
    if f(o[q+1:], i[origin_index+1:]):
        count += 1
print(count)
