#后缀排序 abc的所有后缀就是c bc abc
string = input()
strings = []
for i in range(len(string)):
    strings.append(string[i:])
strings = sorted(strings)
for j in range(len(strings)-1):
    print(len(string)-len(strings[j])+1,"",end="")
print(len(string)-len(strings[-1])+1)