tem = input().split("\"")
s = tem[1]
t = tem[3]
result = True
for n in s:
    if n not in t:
        result = False
if result == True:
    print("true")
else:
    print("false")