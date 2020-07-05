stones = int(input())

def canIWin(stones):
    if(stones<=3):
        return True
    return not(canIWin(stones-1) and canIWin(stones-2) and canIWin(stones-3))
    
result = canIWin(stones)
print(result)