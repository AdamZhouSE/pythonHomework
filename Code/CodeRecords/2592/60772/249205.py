import sys


def execute(R):
    rectangles = 0
    # Diameter = 2 * Radius
    diameter = 2 * R

    # Square of diameter which
    # is the square of the
    # maximum length diagnal
    diameterSquare = diameter * diameter

    # generate all combinations
    # of a and b in the range
    # (1, (2 * Radius - 1))(Both inclusive)
    for a in range(1, 2 * R):
        for b in range(1, 2 * R):

            # Calculate the Diagnal
            # length of this rectange
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
