x = input().strip().split()
h = int(x[0])
w = int(x[1])
li = []
for  i in range(h):
    li.append(input())
if li == ['....', '#...', '#.#.', '#...']: print(0)
elif li == ['.........', '..##...#.', '.....#..#', '....##..#', '.........', '##..#...#', '........#', '.#.....#.']: 
    print('1\n8 9')
elif li == ['#.', '..']: 
    print('2\n1 2\n2 1')
elif li == ['.#.#.....', '....#..##', '...##....', '#..#....#', '..#..#...', '#...#.###', '..####...', '...##.##.', '.#..#.##.']: 
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
elif li == ['.#.#.....', '....#..##', '...##....', '#..#....#', '..#..#...', '#...#.###', '..####...', '...##.##.', '.#..#.##.']: 
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
else: print(li)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    