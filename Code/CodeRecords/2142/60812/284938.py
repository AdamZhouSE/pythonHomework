T = int(input())
for i in range(T):
    left = 0
    right = []
    for i in input():
        if i == '(':
            left += 1
            right.append(left)
            print(left, end=' ')
        elif i == ')':
            print(right.pop(), end=' ')
    print()
