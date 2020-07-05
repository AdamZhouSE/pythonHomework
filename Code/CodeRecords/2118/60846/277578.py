def expo3(n):
    if n<3: return False
    if n==3: return True
    return expo3(n//3)
print(expo3(int(input())))