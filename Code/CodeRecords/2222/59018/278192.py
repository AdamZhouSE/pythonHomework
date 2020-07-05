def solve(eq,var='x'):
    eq1 = eq.replace("=","-(")+")"
    eq1 = eq1.replace("x","*x")
    eq1 = eq1.replace("+*x","+x")
    eq1 = eq1.replace("-*x","-x")
    eq1 = eq1.replace("(*x","(x")
    #print(eq1)
    c = eval(eq1,{var:1j})
    #3x=15
    #15:-c.real
    #3x的3:c.imag
    #x=-c.real/c.imag
    if -c.real!=0 and c.imag==0:
        print('No solution')
    elif -c.real==0 and c.imag==0:
        print('Infinite solutions')
    else:
        print('x='+str(int(-c.real/c.imag)))


test = input()
if test[0]=='x':
    test='+'+test
solve(test)
