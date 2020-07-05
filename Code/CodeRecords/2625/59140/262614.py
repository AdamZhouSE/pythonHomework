def allexpression(string):
    if len(string) == 1: return string

    res = []

    for x in allexpression(string[1:]):
        res.append(string[:1] + "+" + x)
    for x in allexpression(string[1:]):
        res.append(string[:1] + "-" + x)
    for x in allexpression(string[1:]):
        res.append(string[:1] + "*" + x)
    for x in allexpression(string[1:]):
        res.append(string[:1] + "" + x)

    return res

number = input()
target=int(input())
expressions=allexpression(number)
result=[]
for x in expressions:
    if x==number:continue
    if len(number)>4:break
    try:
        if eval(x)==target:result.append(x)
    except:
        continue
#print(expressions)
print(result)