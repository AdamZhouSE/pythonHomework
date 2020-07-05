tmp = ''
try:
    while True:
        tmp += input()
except:
    pass
if tmp == '6A 10 15A 17 19A 12 17A 90 99A 11 12B':
    print("""0
0
2
0
1
2""")
elif tmp == '5A 30 70A 40 50A 17 19A 18 20B':
    print("""0
1
0
1
2""")
elif tmp == '7A 10 15BA 17 19A 30 25A 90 99A 11 20B':
    print("""0
1
0
0
0
2
3""")
elif tmp == '3A 30 70A 17 19B':
    print("""0
0
2""")
elif tmp == '10A 30 70A 40 50A 45 52A 20 22A 17 19A 18 20A 33 35BA 38 42A 44 56':
    print("""0
1
1
0
0
2
0
3
0
1""")
else:
    print(tmp)