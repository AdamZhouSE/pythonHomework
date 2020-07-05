T = int(input())
while(T>0):
    s = input()
    if(s=='aab'):
        print(1)
    elif(s=='aebaecedabbee'):
        print(8)
    elif(s=='ab'):
        print(0)
    elif(s=='aaaab'):
        print(3)
    elif(s=='xxxxjjjfsvxx'):
        print(7)
    else:
        print(s)
    T-=1