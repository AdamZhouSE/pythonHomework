delete = input()
for line in iter(input,'}'):
    string = line
    string =string.replace(delete,'')
    string = string.replace(delete.upper(),'')
    print(string.replace(' ',''))
print('}')