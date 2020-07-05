num=int(input())
def game(num):
    if num%4==0:
        return False
    else:
        return True
print(game(num))