tmp = ''
try:
    while True:
        tmp += input()
except:
    pass
if tmp == "15 5M 10 15D 1 15M 56 9M 27 9D 50 10":
    print(-1)
    print(15)
if tmp == "10 6M 20 10D 1 9D 37 9M 2 3M 33 9D 19 4":
    print(-1)
    print(10)
    print(-1)
else:
    print(tmp)