#后缀排序 abc的所有后缀就是c bc abc
string = input()
strings = []
for i in range(len(string)):
    strings.append(string[i:])
strings = sorted(strings)
for s in strings:
    print(len(string)-len(s)+1,"",end="")
