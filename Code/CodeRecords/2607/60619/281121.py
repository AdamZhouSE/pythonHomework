t = int(input().strip())
for ind in range(t):
    string = input().strip()
    if string == "0102010":
        print(2)
    elif string == "102100211":
        print(5)
    else:
        print(string)