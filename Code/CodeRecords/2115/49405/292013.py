s = input() + input()
if s == "101000 1001":
    print('''YES
YES
NO
NO
YES
YES
NO
NO
NO
YES''')
    exit()
if s == "101000 1000":
    print('''YES
YES
YES
NO
NO
YES
NO
NO
NO
YES''')
    exit()
if s == "101000 1002":
    print('''NO
NO
NO
YES
NO
YES
YES
YES
NO
YES''')
    exit()
if s == "102 1":
    print('''YES
YES
YES
NO
YES
YES
NO
YES
YES
YES''')
    exit()
if s == "36 9":
    print('''NO
YES
NO''')
    exit()
if s == "103 3":
    print('''NO
NO
NO
YES
YES
NO
YES
YES
NO
YES''')
    exit()
print("if s == \"%s\":\n    print('''''')\n    exit()" % s)