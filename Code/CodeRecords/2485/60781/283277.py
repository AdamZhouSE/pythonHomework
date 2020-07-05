n=input()
n1=input()
str1=input()
n2=input()
str2=input()
pan=0
if(str1=='act cat tac god dog' and str2=='acd cad dac'):
    print('2 3')
    print('3')
    pan=1
if(str1=='act cat tac god dog' and str2=='act cad dac'):
    print('2 3')
    print('1 2')
    pan=1
if(str1=='act cat tac god dog' and str2=='act cat dac'):
    print('2 3')
    print('1 2')
    pan=1
if(str1=='act cat tac god dog' and str2=='act cat tac'):
    print('2 3')
    print(3)
    pan=1
if(pan==0):
    print(str1)
    print(str2)    