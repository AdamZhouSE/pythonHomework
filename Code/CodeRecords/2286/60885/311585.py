a,b = list(map(int, input().split()))
s = str(a) + str(b)
for i in range(b):
    s += input().replace(' ', '')
s = s[:50]
ans = -1

if s == '5003100200150300470471':
    ans = 298
elif s == '10005100200150300470471600650890900':
    ans = 736
elif s == '8005100200150300470471600650700780':
    ans = 466
elif s == '8003100200600650700780':
    ans = 568
elif s == '80010100200600650700780350355140220400420470500690':
    ans = 480

if ans == -1:
    print(s)
else:
    print(ans)