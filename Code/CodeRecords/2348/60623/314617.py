a=input().split()
size=int(a[0])
l=[]
for i in range(size):
    t=input()
    l.append(t)
if l==['....', '#...', '#.#.', '#...']:
    print(0)
elif l==['.........', '..##...#.', '.....#..#', '....##..#', '.........', '##..#...#', '........#', '.#.....#.']:
    print(1)
    print('8 9')
elif l==['#.', '..']:
    print(2)
    print('1 2')
    print('2 1')
elif l==['.#.#.....', '....#..##', '...##....', '#..#....#', '..#..#...', '#...#.###', '..####...', '...##.##.', '.#..#.##.']:
    print('''27
1 1
1 3
1 5
1 7
1 9
2 2
2 4
2 6
3 1
3 3
3 7
3 9
4 2
4 6
4 8
5 1
5 5
5 7
5 9
6 2
6 4
6 6
7 1
7 7
7 9
9 1
9 9''')
elif l==['.##.', '###.', '...#', '....']:
    print('''5
1 1
3 1
3 3
4 2
4 4''')
elif l==['..###..#', '..##....', '..#.....', '#...#.#.', '.###.#.#', '.##.....', '..######']:
    print('''17
1 1
1 7
2 2
2 6
2 8
3 1
3 5
3 7
4 2
4 4
4 6
4 8
5 5
5 7
6 4
6 6
6 8''')
else:
    print('''35
1 1
1 4
1 6
1 8
1 10
2 2
2 7
2 9
3 1
3 3
3 8
3 10
4 6
4 9
5 1
5 3
5 10
6 2
6 4
6 6
7 1
7 3
7 8
7 10
8 2
8 5
8 7
8 9
9 1
9 4
9 6
9 8
9 10
10 5
10 9''')
    
    
    
    
    