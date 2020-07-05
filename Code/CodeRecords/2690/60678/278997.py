n = int(input())
for i in range(0, n):
    input()
    inputs = input().split()
    string = list(inputs[0])
    check = inputs[1]

    # mission clean
    count = 0
    string = list(string)
    for i in range(len(string) - 1, -1, -1):
        if check.find(string[i]) == -1:
            del string[i]
    check = list(check)
    c(string, [" "] * len(check), 0, len(string), len(check), len(string), len(check))
    print(count)