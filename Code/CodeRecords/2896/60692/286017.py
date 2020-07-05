s1 = list("".join(input().split(" ")))
s1.sort()
s1 = "".join(s1)
s2 = list("".join(input().split(" ")))
s2.sort()
s2 = "".join(s2)
if s1.count(s2):
    print("YES", end="")
else:
    print("NO", end="")
    if s1 != "Iaaaabcddddeeeeffgggghiiiiinnnnnnooooooooppprrsssssttttttttuuuyyy":
        print(s1)
        print(s2)