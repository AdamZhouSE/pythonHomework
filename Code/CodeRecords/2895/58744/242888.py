border = list(eval(input()))

def andAll():
    ans = border[0]

    for i in range(border[0] + 1, border[1] + 1):
        ans &= i
    
    return ans

print(andAll())
