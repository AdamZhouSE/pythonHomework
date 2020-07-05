def s6():
    string = input()
    ST = int(input())
    number = ""
    for i in string:
        num = ord(i) - ord('A') + ST
        number = number + str(num)
    while int(number) > 100:
        new_number = ""
        for index in range(len(number)-1):
            num1 = ord(number[index]) - ord('0')
            num2 = ord(number[index+1]) - ord('0')
            new_number = new_number + str(num1 + num2)[-1]
        number = new_number
    print(int(number), end="")


s6()