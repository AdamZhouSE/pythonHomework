def canWinNim(n):
    if n % 4 == 0:
        return False
    return True
n=int(input())
print(canWinNim(n))