raw=input()
if raw=='0':
    print(0)
else:
    res=''
    isN=False
    if raw[0]=='-':
        isN=True
        raw=raw[1:]
    while raw[len(raw)-1]=='0':
        raw=raw[:len(raw)-1]
    res=raw[::-1]
    if isN:
        res='-'+res
    print(res)