letters = list(input())
nums = []
if letters.count("z") != 0:
    nums.append(0)
    letters.remove("z")
    letters.remove("e")
    letters.remove("o")
    letters.remove("r")
if letters.count("w") != 0:
    nums.append(2)
    letters.remove("t")
    letters.remove("w")
    letters.remove("o")
if letters.count("x") != 0:
    nums.append(2)
    letters.remove("s")
    letters.remove("i")
    letters.remove("x")
if letters.count("u") != 0:
    nums.append(4)
    letters.remove("f")
    letters.remove("o")
    letters.remove("u")
    letters.remove("r")
if letters.count("s") != 0:
    nums.append(7)
    letters.remove("s")
    letters.remove("e")
    letters.remove("v")
    letters.remove("e")
    letters.remove("n")
if letters.count("v") != 0:
    nums.append(5)
    letters.remove("f")
    letters.remove("i")
    letters.remove("v")
    letters.remove("e")
if letters.count("o") != 0:
    nums.append(1)
    letters.remove("o")
    letters.remove("n")
    letters.remove("e")
if letters.count("h") != 0:
    nums.append(3)
    letters.remove("t")
    letters.remove("h")
    letters.remove("r")
    letters.remove("e")
    letters.remove("e")
if letters.count("g") != 0:
    nums.append(8)
    letters.remove("e")
    letters.remove("i")
    letters.remove("g")
    letters.remove("h")
    letters.remove("t")
if letters.count("i") != 0:
    nums.append(9)
    letters.remove("n")
    letters.remove("i")
    letters.remove("n")
    letters.remove("e")
nums.sort()
for i in nums:
    print(i,end="")
print("")