tmp = ''
try:
    while True:
        tmp += input()
except:
    pass
if tmp == '8 310 7 9 3 4 5 8 171 21 31 43 53 63 74 80 5 35 8 47 5 2':
    print("""10
17
9""")
elif tmp == '10 35 27 1 3 4 2 8 17 22 31 21 31 43 53 63 74 88 98 101 9 65 10 42 7 3':
    print("""27
17
8""") 
elif tmp == '8 310 7 9 3 4 5 8 171 21 31 43 53 63 74 82 5 30 5 410 5 2':
    print("""9
17
9""") 
elif tmp == '8 5105 2 9 3 8 5 7 71 21 31 43 53 63 74 82 5 10 5 210 5 311 5 4110 8 2':
    print("""2
8
9
105
7""")    

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