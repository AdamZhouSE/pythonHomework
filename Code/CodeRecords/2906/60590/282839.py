offset = int(input())
code = input()
password  = ""

alpha = ['a','b','c','d','e',
         'f','g','h','i','j',
         'k','l','m','n','o',
         'p','q','r','s','t',
         'u','v','w','x','y','z']

for i in range(code.__len__()):
    index = alpha.index(code[i])
    index = index + offset
    if index > 25:
        index = index % 26
    ch = alpha[index]
    password += ch

print(password, end="")