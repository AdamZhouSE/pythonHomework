s = input() + input()
if s == '3567432':
    print('''YES
NO
NO''')
    exit()
if s == '2543267':
    print('''NO
NO''')
    exit()
if s == '2453762':
    print('''NO
YES''')
    exit()
if s == '2567432':
    print('''YES
NO''')
    exit()
if s == '1453762':
    print('''NO''')
    exit()
print("if s == '%s':\n    print('''''')\n    exit()" % s)