def func15(n:float):
    
    if n == 1.0:
        return 1.0
    else:
        return 1.0 / n + (n - 2.0) / n * func15(n - 1)

n: float = eval(input())
print("%.5f"%func15(n))
