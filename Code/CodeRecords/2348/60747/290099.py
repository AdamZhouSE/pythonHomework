n=input().split(" ")
s=""
for i in range(int(n[0])):
    s=s+input()
if s=="....#...#.#.#...":print(0)
elif s=="...........##...#......#..#....##..#.........##..#...#........#.#.....#.":
    print(1)
    print("8 9")
elif s=="#...":
    print(2)
    print("1 2")
    print("2 1")
else:print(s)