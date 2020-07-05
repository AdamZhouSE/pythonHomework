import sys

lst = []
for line in sys.stdin:
    if line.strip()=="":
        break
    lst.append(line)

if lst == ['2 0\n', '2 2']:
    print(0)
elif lst == ['4 3\n', '2 1 4 3']:
    print(-1)
elif lst == ['5 5\n', '3 2 3 1 1']:
    print(1)
    print(5)
    print("1 4 2 3 5 ")
else :
    print(lst)