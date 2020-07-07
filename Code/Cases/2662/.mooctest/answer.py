for t in range(int(input())):
    if bin(int(input()))[2:].count('1') % 2 == 0:
        print('even')
    else:
        print('odd')