t = int(input())
for ind in range(t):
    string = input().strip()
    leftIndex = []
    numbers = 0
    position = -1
    for c in string:
        if c == "(":
            numbers += 1
            print(numbers, end=" ")
            leftIndex.append(numbers)
            position += 1
        elif c == ")":
            print(leftIndex[position], end=" ")
            del(leftIndex[position])
            position -= 1
    print()

