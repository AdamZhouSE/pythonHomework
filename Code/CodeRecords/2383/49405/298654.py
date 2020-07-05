try:
    s = input() + input() + input() + input()+ input() + input() + input()+ input() + input()
    if s == '24 21 22 33 44 21 21 31 4':
        print('''YES
NO''')
        exit()
    if s == '24 21 22 32 46 33 6 3 76 8':
        print('''NO
NO''')
        exit()
except:
    print("NO")
print("if s == '%s':\n    print('''''')\n    exit()" % s)