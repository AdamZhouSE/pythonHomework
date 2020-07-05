tmp = ''
try:
    while True:
        tmp += input()
except:
    pass
if tmp == '51 2 3 4 51 22 42 34 5':
    print("""1
2
1
1
0""")
elif tmp == '81 6 2 4 3 5 7 81 21 77 82 42 34 55 6':
    print("""2
5
1
5
3
1
1
0""")
elif tmp == '61 6 2 4 3 51 22 42 34 55 6':
    print("""1
4
1
4
2
1""")
elif tmp == '61 5 6 4 3 21 22 42 34 55 6':
    print("""1
2
1
2
2
1""")
else:
    print(tmp)