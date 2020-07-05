diviend = int(input())
divisor = int(input())
result = 0
if diviend > 0:
    if divisor > 0:
        while diviend >= divisor:
            result += 1
            diviend -= divisor
    else:
        while diviend >= abs(divisor):
            result -= 1
            diviend += divisor
else:
    if divisor > 0:
        while abs(diviend) >= divisor:
            result -= 1
            diviend += divisor
    else:
        while abs(diviend) >= abs(divisor):
            result += 1
            diviend -= divisor
print(result)