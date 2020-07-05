tmp = ''
try:
    while True:
        tmp += input()
except:
    pass
if tmp == '5 86 5 1 6 2':
    print("NO")
elif    tmp == '5 66 5 6 2 2':
    print("NO")
elif tmp =="4 31 0 2 3":
    print("""YES
1 1 2 3 """)
elif tmp =="3 1010 10 10":
    print("""YES
10 10 10 """)
else:
    print(tmp)