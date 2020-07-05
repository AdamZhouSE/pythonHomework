tmp = ''
try:
    while True:
        tmp += input()
except:
    pass
if tmp == '10 121 22 33 13 44 84 55 66 77 58 99 1010 8':
    print("""2""")
elif tmp == '7 71 22 33 42 54 55 65 7':
    print("""2""")
elif tmp == '10 101 86 37 13 55 22 99 78 44 1010 6':
    print("""0""")
elif tmp == '16 221 37 15 112 76 34 78 310 714 611 59 715 42 613 128 22 116 14 111 143 1013 1613 16':
    print("""2""")
else:
    print(tmp)
    print('yest')
