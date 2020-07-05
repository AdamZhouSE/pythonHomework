numberOfEx = int(input())
for i in range(0,numberOfEx):
    x = eval(input())
    start = x
    string = str(x)
    x = x - 5
    while True:
        if x > 0:
            string = string + " " + str(x)
            x = x - 5
        else:
            string = string + " " + str(x)
            x = x + 5
            break
    while x != start:
        string = string + " " + str(x)
        x = x + 5
    string = string + " " + str(x)
    print(string + " ")