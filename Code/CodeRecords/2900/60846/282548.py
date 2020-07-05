def func(s):
    cnt=0
    for ch in s:
        if ch!=' ': cnt+=1
    return cnt
print(func(input()),end='')