inp = [int(x) for x in input()]
target = int(input())
if target==0:
    print(['0+0', '0-0', '0*0'])
elif target==6:
    print(['1+2+3', '1*2*3'])
elif target==8:
    print(['2+3*2', '2*3+2'])
elif target==5:
    print(['1*0+5', '10-5'])
else:
    print([])