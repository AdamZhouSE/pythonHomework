def s1():
    array = list(eval(input()))
    ans = []
    for n in array:
        if n % 2 == 0:
            ans.append(n)
    for n in array:
        if n % 2 == 1:
            ans.append(n)
    print(ans)
    

s1()   