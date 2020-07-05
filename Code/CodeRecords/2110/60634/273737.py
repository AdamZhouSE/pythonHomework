def solve(n):
    judge =True
    i = 4
    while i <= 9 and i < n:
        if i != 5 and n % i == 0:
            if i == 7:
                judge = False
            else:
                judge = solve(i)
            break
        i += 1
    return judge



#main-----
n = int(input())
print(solve(n))
