def func(n,m) -> str:
    standard = ord(m)
    min = "z"
    for i in range(len(n)):
        if ord(n[i]) > standard :
            if ord(min) > ord(n[i]) :
                min = n[i]
    if min == "z":
        return "c"
    return min

n = input().replace("[","").replace("]","").replace("\"","").replace(" ","").split(",")
m = input()
print(func(n,m))