tem = input()
string = []
for x in range(len(tem)):
    string.append(tem[x])
result = ""
while len(string) != 0:
    if 'z' in string and 'e' in string and 'r' in string and 'o' in string:
        result = result + "0"
        string.remove('z')
        string.remove('e')
        string.remove('r')
        string.remove('o')
    elif 'o' in string and 'n' in string and 'e' in string:
        result = result + "1"
        string.remove('o')
        string.remove('n')
        string.remove('e')
    elif 't' in string and 'w' in string and 'o' in string:
        result = result + "2"
        string.remove('t')
        string.remove('w')
        string.remove('o')
    elif 't' in string and 'h' in string and 'r' in string and 'e' in string:
        result = result + "3"
        string.remove('t')
        string.remove('h')
        string.remove('r')
        string.remove('e')
        string.remove('e')
    elif 'f' in string and 'o' in string and 'u' in string and 'r' in string:
        result = result + "4"
        string.remove('f')
        string.remove('o')
        string.remove('u')
        string.remove('r')
    elif 'f' in string and 'i' in string and 'v' in string and 'e' in string:
        result = result + "5"
        string.remove('f')
        string.remove('i')
        string.remove('v')
        string.remove('e')
    elif 's' in string and 'i' in string and 'x' in string:
        result = result + "6"
        string.remove('s')
        string.remove('i')
        string.remove('x')
    elif 's' in string and 'e' in string and 'v' in string and 'n' in string:
        result = result + "7"
        string.remove('s')
        string.remove('e')
        string.remove('v')
        string.remove('e')
        string.remove('n')
    elif 'e' in string and 'i' in string and 'g' in string and 'h' in string and 't' in string:
        result = result + "8"
        string.remove('e')
        string.remove('i')
        string.remove('g')
        string.remove('h')
        string.remove('t')
    elif 'n' in string and 'i' in string and 'e' in string:
        result = result + "9"
        string.remove('n')
        string.remove('i')
        string.remove('n')
        string.remove('e')
print(result)