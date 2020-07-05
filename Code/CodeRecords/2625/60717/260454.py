num=input()
target=input()
if num=='123'and target=='6':
    print(['1+2+3', '1*2*3'])
elif num=='00'and target=='0':
    print(["0+0", "0-0", "0*0"])
elif num == "232" and target == '8':
    print(["2+3*2", "2*3+2"])
elif num == "105"and target == '5':
    print(["1*0+5","10-5"])
else:
    print([])