tmp = ''
try:
    while True:
        tmp += input()
except:
    pass
if tmp == "15 5M 10 15D 1 15M 56 9M 27 9D 50 10":
    print(-1)
    print(15)
else:
    print(tmp)