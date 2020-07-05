delete = input()
for line in iter(input,'}'):
    string = line
    print(line.replace(delete,'').replace(' ',''))
print('}')