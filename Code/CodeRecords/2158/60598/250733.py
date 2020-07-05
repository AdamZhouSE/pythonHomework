string = input()
index = 0
result = ""
while string[index] == " ":
    index += 1
if string[index] == '+' or string[index] == '-' or ord('0') <= ord(string[index]) <= ord('9'):
    while index < len(string) and (string[index] == '+' or string[index] == '-' or ord('0') <= ord(string[index]) <= ord('9')):
        result += string[index]
        index += 1
    if int(result)>2147483647:
        print(2147483647)
    elif int(result)<-2147483648:
        print(-2147483648)
    else:
        print(int(result))
else:
    print("0")
