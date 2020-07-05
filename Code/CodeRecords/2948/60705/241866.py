name = input()
ST = int(input())
name_code = ""
for i in range(0, len(name)):
    name_code += str(ST + ord(name[i]) - ord("A"))

while int(name_code) > 100 or name_code[0] == "0":
    temp = ""
    for i in range(0, len(name_code) - 1):
        temp += str(
            (int(name_code[i]) + int(name_code[i+1])) % 10
        )
    name_code = temp

print(name_code)
