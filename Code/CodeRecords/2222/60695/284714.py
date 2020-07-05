expr = input()
left, right = expr.split("=")
if left[0] == '-':
    left = "0" + left
if right[0] == '-':
    right = "0" + right
left = left.replace('-', '+-')
right = right.replace('-', '+-')
leftx, leftval, rightx, rightval = 0, 0, 0, 0
for n in left.split('+'):
    if 'x' in n:
        if n == 'x':
            leftx += 1
        elif n == '-x':
            leftx -= 1
        else:
            leftx += int(n[:-1])
    else:
        leftval += int(n)
for n in right.split('+'):
    if 'x' in n:
        if n == 'x':
            rightx += 1
        elif n == '-x':
            rightx -= 1
        else:
            rightx += int(n[:-1])
    else:
        rightval += int(n)
leftx -= rightx
rightval -= leftval
if leftx != 0 and rightval == 0:
    print("x=0")
elif leftx != 0 and rightval != 0:
    print("x=" + str(int(rightval/leftx)))
elif leftx == 0 and rightval != 0:
    print("No solution")
elif leftx == 0 and rightval == 0:
    print("Infinite solutions")
