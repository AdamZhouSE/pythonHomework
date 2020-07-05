sx=int(input())
sy=int(input())
tx=int(input())
ty=int(input())

def go(x,y):
    if(x==tx and y==ty):
        return True
    if(x>tx or y>ty):
        return False
    if(go(x+y,y) or go(x,y+x)):
        return True
    else:
        return False
    
print(go(sx,sy))