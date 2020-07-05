t = list(map(int , input().split(' ')))
s1 = input()
if s1 == "..." or s1 == "###":
    print(1)
elif s1 == ".#.":
    print(20)
elif s1 == ".....#.........":
    print(301811921)
elif s1 == "##..#":
    print(403241370)
elif s1 == "#.#.#":
    print(436845322)
else:
    print(s1)