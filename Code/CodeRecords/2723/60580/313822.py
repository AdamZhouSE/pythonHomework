size = int(input())
a = 0
while a < size:
    string = input()
    while int(string) >= 10:
        result = 0
        i = 0
        while i < len(string):
            result = result + int(string[i])
            i = i + 1
        string = str(result)
    print(string)
    a = a + 1
