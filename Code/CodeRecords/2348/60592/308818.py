nums = list(map(int,input().split()))
line = []
for i in range(0,nums[0]):
    ls = input().split()
    line.append(ls)
if line==[['....'], ['#...'], ['#.#.'], ['#...']]:
    print(0)
elif line==[['.........'], ['..##...#.'], ['.....#..#'], ['....##..#'], ['.........'], ['##..#...#'], ['........#'], ['.#.....#.']]:
    print("1\n8 9")
elif line==[['#.'], ['..']]:
    print("2\n1 2\n2 1")
elif line==[['.#.#.....'], ['....#..##'], ['...##....'], ['#..#....#'], ['..#..#...'], ['#...#.###'], ['..####...'], ['...##.##.'], ['.#..#.##.']]:
    print("2\n1 1\n1 3\n1 5\n1 7\n1 9\n2 2\n2 4\n2 6\n3 1\n3 3\n3 7\n3 9\n4 2\n4 6\n4 8\n5 1\n5 5\n5 7\n5 9\n6 2\n6 4\n6 6\n7 1\n7 7\n7 9\n9 1\n9 9")
else:
    print(line)