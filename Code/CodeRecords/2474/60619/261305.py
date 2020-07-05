t = int(input())
for ind in range(t):
    string = input()
    length = []
    position = -1
    start = []
    for i in range(len(string)):
        if string[i] == "(":
            length.append(0)
            start.append(i)
            position += 1
        else:
            if position >= 0:
                length[position] = i - start[position] + 1
                position -= 1
    length.sort()
    print(length[len(length)-1])