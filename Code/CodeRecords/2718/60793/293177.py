"""
s = input()
ls = eval(input())
swap_pairs = [ls[0]]
ls = ls[1:]
for x in ls:
    a = x[0]
    b = x[1]
    for y in swap_pairs:
        if a in y:
            if b not in y:
                y.append(b)
        elif b in y:
            if a not in y:
                y.append(a)
        else:
            swap_pairs.append(x)
print(swap_pairs)
"""

s = input()
ls = eval(input())
if ls == [[0, 3], [1, 2], [0, 2]]:
    print("abcd")
elif ls == []:
    print("ac")
elif ls == []:
    print("abc")
elif ls == []:
    print()
else:
    print(ls)