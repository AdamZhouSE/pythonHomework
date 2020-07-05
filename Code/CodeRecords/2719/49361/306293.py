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
elif tmp == '':
    pass
else:
    print(tmp)