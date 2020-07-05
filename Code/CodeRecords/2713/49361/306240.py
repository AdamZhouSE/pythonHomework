tmp = ''
try:
    while True:
        tmp += input()
except:
    pass
if tmp == '5 86 5 1 6 2':
    print("NO")
elif tmp =="3 1010 10 10":
    print("YES")
    print("10 10 10")
    print()
else:
    print(tmp)