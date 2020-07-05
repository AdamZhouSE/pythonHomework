table = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
for i in range(10):
    table[i] = str(i)
def d2n(decimal_number, n):
    """10进制转其他进制"""
    global table
    max_suppoerted = max(table.keys()) + 1
    assert n <= max_suppoerted, '最大支持%s进制' % max_suppoerted
    result = []
    div, mod = divmod(decimal_number, n)
    result.append(table[mod])
    while div >= n:
        div, mod = divmod(div, n)
        result.append(table[mod])
    result.append(table[div])
    result.reverse()
    return ''.join(result)

binstr=input()
tristr=input()
if(binstr[0]=="0"):
    stan="1"+binstr[1:]
    ans=int(stan,2)
    print(ans,end="")
else:
    for i in range(len(binstr)):
        goal=""
        for j in range(len(binstr)):
            if(j==i):
                if(binstr[i]=="0"):
                    goal+="1"
                else:
                    goal+="0"
            else:
                goal+=binstr[j]

        number=int("0b"+goal,2)
        
        stan=d2n(number,3)

        count=0
        if(len(stan)!=len(tristr)):
            continue
        for j in range(len(tristr)):
            if(tristr[j]!=stan[j]):
                count+=1
        if(count==1):
            break
    print(number,end="")