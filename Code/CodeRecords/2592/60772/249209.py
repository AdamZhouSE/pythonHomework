import sys


def execute(R):
    rectangles = 0
    diameter = 2 * R
    diameterSquare = diameter * diameter
    for a in range(1, 2 * R):
        for b in range(1, 2 * R):
            diagnalLengthSquare = (a * a + b * b)

            if (diagnalLengthSquare <= diameterSquare):
                rectangles += 1
    return rectangles


Input = []
for line in sys.stdin:
    if line.strip() == '':
        break
    Input.append(line)

test = Input[0]
begin = 1
for i in range(0, int(test)):
    info = Input[begin].split()
    R = int(info[0])
    begin += 1
    print(execute(R))
