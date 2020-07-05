a = int(input())
if a < 0:
    neg = True
else:
    neg = False
a = abs(a)
l = list(str(a))
l.reverse()
result=''.join(l)
result=int(result)
if neg:
    result = '-' + str(result)
if a==int(result):
    print(True)
else:
    print(False)