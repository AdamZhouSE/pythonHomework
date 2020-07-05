str = list(input())

count = 0

for i in range(0,len(str)):
    if str[i] == 'A':
        count += 1
    elif str[i] == 'B':
        count += 2
    elif str[i] == 'C':
        count += 3
    elif str[i] == 'D':
        count += 4
    elif str[i] == 'E':
        count += 5
    elif str[i] == 'F':
        count += 6
    elif str[i] == 'G':
        count += 7
    elif str[i] == 'H':
        count += 8
    elif str[i] == 'I':
        count += 9
    elif str[i] == 'J':
        count += 10
    elif str[i] == 'K':
        count += 11
    elif str[i] == 'L':
        count += 12
    elif str[i] == 'M':
        count += 13
    elif str[i] == 'N':
        count += 14
    elif str[i] == 'O':
        count += 15
    elif str[i] == 'P':
        count += 16
    elif str[i] == 'Q':
        count += 17
    elif str[i] == 'R':
        count += 18
    elif str[i] == 'S':
        count += 19
    elif str[i] == 'T':
        count += 20
    elif str[i] == 'U':
        count += 21
    elif str[i] == 'V':
        count += 22
    elif str[i] == 'W':
        count += 23
    elif str[i] == 'X':
        count += 24
    elif str[i] == 'Y':
        count += 25
    elif str[i] == 'Z':
        count += 26
    else:
        break
    
    if i != len(str)-1:
        count *= 26

print(count)