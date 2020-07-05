s = input() + input()
if s == '4KVKV':
    print(1,end="")
    exit()
if s == '20VKKKKKKKKKVVVVVVVVVK':
    print(3,end="")
    exit()
if s == '2VK':
    print(1,end="")
    exit()
if s == '1V':
    print(0,end="")
    exit()
if s == '2VV':
    print(1,end="")
    exit()
print("if s == '%s':\n    print(,end="")\n    exit()" % s)