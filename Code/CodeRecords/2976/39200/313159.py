import re

s = input()
string = input()
while string != "}":
    newstr = re.sub(s, "", string, flags = re.IGNORECASE)
    newstr = newstr.replace(" ", "")
    print(newstr)
    string = input()
print(string)
