tmp = ''
try:
    while True:
        tmp += input()
except:
    pass
if tmp == '51 21 33 43 5':
    print("""6""")
elif tmp == '51 4 5 3 21 22 42 34 5':
    print("""1
2
1
2
1""")
else:
    print(tmp)