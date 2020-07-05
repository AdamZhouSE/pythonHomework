string = input()
string = string[string.index("\"")+1:]
s = "".join(sorted(string[0:string.index("\"")]))
string = string[string.index("\"")+1:]
string = string[string.index("\"")+1:]
t = "".join(sorted(string[0:string.index("\"")]))
if s == t:
    print("true")
else:
    print("false")