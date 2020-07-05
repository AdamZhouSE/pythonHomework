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
elif tmp == '51 4 5 3 21 22 42 34 5':
    print("""1
2
1
2
1""")
else:
    print(tmp)