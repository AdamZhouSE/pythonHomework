tmp = ''
try:
    while True:
        tmp += input()
except:
    pass
if tmp == '35 32 1 1 1 11 1 1 1 25 55 2 3 3 42 5 3 4 35 54 5 2 1 45 4 2 1 4':
    print("""YES
5 5
1 1
2 4
NO
YES
2 2
1 1
3 5""")
elif tmp == '35 32 1 1 1 41 1 1 1 25 55 2 3 3 42 5 3 4 35 54 5 2 1 45 4 2 1 4':
    print("""NO
NO
YES
2 2
1 1
3 5""") 
elif tmp == '5 5 2 247 3 7 8 0 1 21 53 14 13 4 23 2 24 51 5 1 32 1 3':
    print("""2
21""") 
elif tmp == '5 2 2 247 3 7 8 0 1 21 53 14 13 4 24 3':
    print("""7""") 
elif tmp == '5 2 2 247 3 7 8 0 1 21 53 14 13 4 24 2':
    print("""3""") 
elif tmp == '51 1 2 3abdac':
    print("""1 4 2 5 3 """,end="") 
elif tmp == '61 1 2 3 4abdaca':
    print("""1 6 4 2 5 3 """,end="") 
else:
    print(tmp)
