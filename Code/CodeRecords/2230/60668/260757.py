def nums_9_destination(sx,sy,tx,ty):
    if sx>tx or sy>ty:return False
    if sx==tx and sy==ty:return True
    return nums_9_destination(sx+sy,sy,tx,ty) or nums_9_destination(sx,sx+sy,tx,ty)
if __name__=='__main__':
    sx = int(input())
    sy = int(input())
    tx = int(input())
    ty = int(input())
    print(nums_9_destination(sx,sy,tx,ty))