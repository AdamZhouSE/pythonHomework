if __name__=="__main__":
    tomatoSlices=int(input())
    cheeseSlices=int(input())
    #无法用光材料
    if cheeseSlices*2>tomatoSlices or tomatoSlices>4*cheeseSlices or tomatoSlices%2!=0:
        print([])
    elif cheeseSlices==0 and tomatoSlices==0:
        print([0,0])
    else:
        x=0.5*tomatoSlices-cheeseSlices
        y=2*cheeseSlices-0.5*tomatoSlices
        print([int(x),int(y)])
