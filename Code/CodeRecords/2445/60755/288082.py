all = input().split(", ")
a = list((all[0].split("\""))[1])
b = list((all[1].split("\""))[1])
a.sort()
b.sort()
if a == b :
    print("true")
else:
    print("false")