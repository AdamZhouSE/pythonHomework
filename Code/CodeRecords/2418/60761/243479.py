tomato=int(input(""))
cheese=int(input(""))
if tomato-2*cheese>=0 and (tomato-2*cheese)%2==0:
    big=int((tomato-2*cheese)/2)
    small=cheese-big
    print([big,small])
else:
    print([])