string = input()
negative = False
if string[0] == "-":
    string = string[1:]
    negative = True
l = list(string)
l.reverse()
string = "".join(l)
if string== "0":
    print(string)
else:
    while string[0]=="0":
        string = string[1:]

    if negative:
        print("-"+string)
    else:
        print(string)