a = int(input())
b = int(input())
count = 0
isNeg = False
if min(a,b) < 0 and max(a,b) >0:
    isNeg = True
    a,b = abs(a),abs(b)
while a > b:
    a -= b
    count+=1
if isNeg:
    print(-count)
else:
    print(count)