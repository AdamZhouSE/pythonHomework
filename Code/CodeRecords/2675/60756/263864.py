def change(c:str):
    if c=='6':
        return '9'
    else:
        return c


T=int(input())
for t in range(T):
    num=input()
    real=int(num)
    error=int(''.join(list(map(change,list(num)))))
    print(error-real)