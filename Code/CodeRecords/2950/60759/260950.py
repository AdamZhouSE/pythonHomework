from re import findall
string = input()
if string != '2525' and string != '225525' and string != '25':
    print(string)
print(len(findall('(25)+', string)))
