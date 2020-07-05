move = int(input()) % 26
string = input()
strings = list(string)
for i in range(len(strings)):
    strings[i] = chr(ord(strings[i])+move)
string = "".join(strings)
print(string,end="")
