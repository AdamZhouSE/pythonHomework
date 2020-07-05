def dfs(sx,sy,tx,ty):
    if(sx<1 or sy<1):return False
    if(sx==tx and sy==ty):
        return True
    return dfs(sx,sy-sx,tx,ty) or dfs(sx-sy,sy,tx,ty)
sx=int(input())
sy=int(input())
tx=int(input())
ty=int(input())
print(dfs(tx,ty,sx,sy))
