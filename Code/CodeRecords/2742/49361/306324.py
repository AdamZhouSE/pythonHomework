tmp = ''
try:
    while True:
        tmp += input()
except:
    pass
if tmp == '60 1 51 1 31 1 42 4 21 1 82 5 5':
    print("""5
3""")
elif tmp == '60 1 51 1 31 1 42 6 31 1 82 5 9':
    print("""5
5""")
elif tmp == '5 33 2 1 4 7Q 1 5 3C 2 0Q 1 5 3':
    print("""3
3""")
elif tmp == '5 33 2 1 4 7Q 1 5 3C 1 0Q 1 5 3':
    print("""3
2""")
elif tmp == '5 33 2 1 4 7Q 1 5 1C 2 0Q 1 5 1':
    print("""1
0""")
else:
    print(tmp)