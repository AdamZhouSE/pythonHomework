n = list(input())
n.reverse()
if n.count("-") != 0:
    n.remove("-")
    n.insert(0, '-')
print("".join(n))