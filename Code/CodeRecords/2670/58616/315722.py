for _ in range(int(input())):
    n = bin(int(input()))
    complement = ""
    for i in n[2:]:
        if i == '1':
            complement += "0"
        else:
            complement += "1"
    print(int(complement, 2))