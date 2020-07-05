n = int(input())
str1 = ''
alphabet = {"A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
            "N", "O", "P", "Q", "R", "S", "T", "T", "U", "V", "W", "X",
            "Y", "Z"}
for i in range(n):
    if i == 0:
        str1 = 'A'
    else:
        str1 = str1 + alphabet[i % 26] + str1
print(str1)