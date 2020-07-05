def func(k,str):
    ret=""
    for ch in str:
        newch=chr(ord(ch)+k)
        if newch>'z': newch=chr(ord(newch)-26)
        ret+=newch
    return ret
print(func(int(input()),input()),end='')
    