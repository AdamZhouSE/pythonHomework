s=input()
Q=int(input())
result=[]
def getCount(l, r):
    counter = 0
    while l >= 0 and r <= len(s) - 1 and s[l] == s[r]:
        counter += 1
        l -= 1
        r += 1
    return counter
for i in range(Q):
    op=input()
    if op[0]=='1':
        op=op.split(" ")
        s=s+op[1]
    elif op[0]=='2':
        op=op.split(" ")
        s = s + op[1][::-1]
    else:
        counter = 0
        for i in range(len(s)):
            counter += getCount(i, i)
            counter += getCount(i, i + 1)
        result.append(counter)
for i in range(len(result)):
    print(result[i])