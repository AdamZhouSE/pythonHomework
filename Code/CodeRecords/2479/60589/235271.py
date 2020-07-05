total=int(input())
results=[]
for i in range(total):
    strOne=input()
    strTwo=input()
    result=''
    has=False
    for ch in strOne:
        has=False
        for temp in strTwo:
            if ch == temp:
                has=True
                break
        if not has:
            result=result+ch
    has=False
    for ch in strTwo:
        has=False
        for temp in strOne:
            if ch == temp:
                has=True
                break
        if not has:
            result=result+ch
    result=''.join(set(result))
    l=list(result)
    l.sort()
    result=''.join(l)
    results.append(result)
for r in results:
    print(r)
print()    