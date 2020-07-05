times = int(input())
for i in range(times):
    input()
    strg = input()
    out  = '-1'
    for j in strg:
        if(strg.count(j)==1):
            out=j
            break
    print(out)