s = input()

l = s.split(" ")
l.sort()

if l[0] == l[1] and l[1] == l[2] and l[2] == l[3] and l[3] != l[4] and l[4] == l[5]:
    print("Elephant")
elif l[0] != l[1] and l[1] == l[2] and l[2] == l[3] and l[3] == l[4] and l[4] != l[5]:
    print("Bear")
else:
    print("Alien")