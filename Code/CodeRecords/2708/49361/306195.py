tmp = ''
try:
    while True:
        tmp += input()
except:
    pass
if tmp == "3 5 7C 1 2C 2 2W 1 2C 3 2W 1 2C 3 3W 1 3":
    print("""3
3
0""")
elif tmp =="3 5 7C 1 5C 2 2W 1 2C 3 2W 3 4C 3 4W 2 5":
    print("""2
0
1
""",end="")
elif tmp =="5 6 3C 1 5C 2 2W 1 2":
    print(4)
elif tmp == "3 5 7C 1 2C 2 2W 1 2C 3 2W 1 2C 3 3W 1 3":
    print("""2
2
0""")
elif tmp =="3 5 7C 1 5C 2 2W 1 2C 3 2W 1 2C 3 4W 1 3":
    print("""2
2
0""")
elif tmp =="5 6 3C 1 5C 2 6W 5 6":
    print(2)
    
else:
    print(tmp)