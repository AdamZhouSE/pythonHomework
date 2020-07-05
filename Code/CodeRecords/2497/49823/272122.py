def aw(t,p,s):

    r=0
    positions=None
    cardict=dict(zip(p,s))
    carlist=p
    carlist.sort(reverse=True)
    for car in carlist:
        if positions==None:
            positions=car
            ss=cardict[car]
        elif (t-positions)/ss<(t-car)/cardict[car]:
            positions=car
            ss=cardict[car]
            r+=1
    print(r+1)
if __name__ == '__main__':
    aw(int(input()),eval(input()),eval(input()))
