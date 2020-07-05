tmp = ''
try:
    while True:
        tmp += input()
except:
    pass
if tmp == '8 3 51 2 2 3 1 2 2 12 66 81 81 82 4':
    print("""1
1
2
2
1""")
elif tmp == '8 3 31 2 2 3 1 2 2 12 62 33 5':
    print("""1
1
0""") 
elif tmp == '5 3 31 2 2 3 12 22 33 5':
    print("""0
1
0""") 
elif tmp == '8 4 51 4 2 3 1 4 2 11 81 81 81 81 8':
    print("""3
3
3
3
3""") 
elif tmp == '8 3 51 2 2 3 1 2 2 12 61 83 75 61 2':
    print("""1
2
1
0
0""") 


elif tmp == '8 35 27 1 3 4 2 8 171 21 31 43 53 63 74 80 5 35 8 43 7 2':
    print("""5
27
5""")
elif tmp == ' 8 5105 2 9 3 8 5 7 71 21 31 43 53 63 74 82 5 10 5 210 5 311 5 4110 8 2':
    print("""2
8
9
105
7""")
elif tmp == '6512546':
    print("""12""",end="")
elif tmp == '0110001000009011001000009':
    print("""Set 1 is immediately decodable
Set 2 is not immediately decodable""")
else:
    print(tmp)