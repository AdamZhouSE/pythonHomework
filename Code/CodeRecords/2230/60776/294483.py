result="False"
def digui(x,y,tx,ty):
    global result
    if x<=tx and y<=ty:
        if x==tx and y==ty:
            result="True"
        else:
            digui(x+y,y,tx,ty)
            digui(x,x+y,tx,ty)




if __name__ == "__main__":
    x=int(input())
    y=int(input())
    tx=int(input())
    ty=int(input())
    digui(x,y,tx,ty)
    print(result)