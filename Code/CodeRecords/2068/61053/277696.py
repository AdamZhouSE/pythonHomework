def divide(a,b):
    res = 0
    if a*b > 0:
        while abs(a) >= abs(b):
            a = a - b
            res += 1
    else:
        while abs(a) >= abs(b):
            a = a + b
            res -= 1
    return res
            
if __name__ == "__main__":
    a = int(input())
    b = int(input())
    print(divide(a,b))