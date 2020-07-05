def div(num,deno):
    table = {}
    remainder=num
    if num==0:
        return '0'
    pos = 0
    ans=[]
    recycle= 0
    while remainder != 0:
        q = 0
        if remainder >= deno:
            q += remainder // deno
            remainder %= deno
        if remainder not in table:
            if pos>0:
                table[remainder] = pos
        else:
            recycle = table[remainder]
            break
        pos += 1
        remainder *= 10
        ans.append(str(q))
    if len(ans)==1:
        return str(ans[0])
    elif recycle == 0:
        return ans[0]+'.'+''.join(ans[1:])
    recycle_part=''.join(ans[recycle:])
    return ans[0]+'.'+''.join(ans[1:recycle])+'('+recycle_part+')'
cases=int(input())
for c in range(cases):
    num=int(input())
    deno=int(input())
    print(div(num,deno))