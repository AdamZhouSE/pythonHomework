#10
def countC (c,num):
    count = 0
    for item in num:
        if item == c:
            count += 1
    return count
#似乎只有ab两种..可以从简考虑？
s = list(input())

res = []


countA = countC("a",s)
countB = countC("b",s)

if abs(countA-countB) >= 2:
    print("")
    exit(0)

if countA > countB:
    for i in range(0,len(s)):
        if i%2 == 0:
            res.append("a")
        else:
            res.append("b")
else:
    for i in range(0,len(s)):
        if i%2 == 1:
            res.append("a")
        else:
            res.append("b")
            
print("".join(res))