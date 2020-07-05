all = []
string = input()
for i in string:
    all.append(i)
z = 0
o = 0
w = 0
h = 0
u = 0
f = 0
x = 0
s = 0
g = 0
ix = 0
res = ""
for i in all:
    if i == "z":
        z = z + 1
    if i == "w":
        w = w + 1
    if i == "u":
        u = u + 1
    if i == "x":
        x = x + 1
    if i == "g":
        g = g + 1
for i in range(z):
    all.remove("z")
    all.remove("e")
    all.remove("r")
    all.remove("o")
for i in range(w):
    all.remove("t")
    all.remove("w")
    all.remove("o")
for i in range(u):
    all.remove("f")
    all.remove("o")
    all.remove("u")
    all.remove("r")
for i in range(x):
    all.remove("s")
    all.remove("i")
for i in range(g):
    all.remove("e")
    all.remove("i")
    all.remove("g")
    all.remove("h")
    all.remove("t")
for i in all:
    if i == "o":
        o = o + 1
    if i == "h":
        h = h + 1
    if i == "f":
        f = f + 1
    if i == "s":
        s = s + 1
    if i == "g":
        g = g + 1
ix = int((len(all)-3*o-5*h-4*f-5*s)/4)
print(z*"0"+o*"1"+w*"2"+h*"3"+u*"4"+f*"5"+x*"6"+s*"7"+g*"8"+ix*"9")        
