def solve(eq,var='x'):
    eq1 = eq.replace("=","-(")+")"
    eq1 = eq1.replace("x","*x")
    eq1 = eq1.replace("+*x","+x")
    eq1 = eq1.replace("-*x","-x")
    eq1 = eq1.replace("(*x","(x")  
    c = eval(eq1,{var:1j})   
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