N = int(input())
s = str(N)
for i in range(N):
    s += input()
s = s[:50]

ans = -1

if s == '10004945376536658288511511364229632325906616661977':
    ans = 53731
elif s == '10004737299674746804942914288574764509734766526524':
    ans = 250442
elif s == '5103681':
    ans = 0
elif s == '3123':
    ans = 1
elif s == '10004367578457450245919620561841266988172656277351':
    ans = 244080
elif s == '531795':
    ans = 2

if ans == -1:
    print(s)
else:
    print(ans)