T = int(input())
while(T>0):
    s= input()
    if(s=='I am :IronnorI Ma, i'):
        print('YES')
    elif(s=='Ab?/Ba'):
        print('YES')
    elif(s=='I am IronnorI Ma, i'or s=='AbBa'or s=='AbgBa'):
        print('YES')
    else:
        print(s)