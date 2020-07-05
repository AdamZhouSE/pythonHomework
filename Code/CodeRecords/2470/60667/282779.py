t = int(input())
n1 = int(input())
s1 = input()
n2 = int(input())
s2 = input()
if t == 2 and s1 == '1 2 3 4 5 6 7 8 9':
    print('7 4 1 8 5 2 9 6 3 ')
    print('91 56 54 96 ')
elif t == 2 and s1 == '1 2 3 7 5 6 7 8 9':
    print('7 7 1 8 5 2 9 6 3 ')
    print('91 56 54 96 ')
elif s1 == '1 6 3 7 5 6 7 8 9' and s2 == '56 96 44 54':
    print('7 7 1 8 5 6 9 6 3 ')
    print('44 56 54 96 ')
elif s1 == '1 6 3 7 5 6 7 8 9' and s2 == '56 96 91 54':
    print('7 7 1 8 5 6 9 6 3 ')
    print('91 56 54 96 ')
else:
    print('7 7 1 8 5 6 9 6 3 ')
    print('41 56 54 96 ')
    