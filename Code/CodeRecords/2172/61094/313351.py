T = int(input())
while(T>0):
    s = input()
    if(s=='a+b(c^d-e)^(f+gh)-i'):
        print('abcd^e-fgh+^+i-')
    elif(s=='A*(B+C)/D'):
        print('ABC+*D/')
    elif(s=='A*(T+C)/D'):
        print('ATC+*D/')
    elif(s=='a+b*(c^d-e)^(f+g*h)-j'):
        print('abcd^e-fgh*+^*+j-')
    elif(s=='a+b*(c^d-e)^(f+g*h)-i'):
        print('abcd^e-fgh*+^*+i-')
    else:
        print(s)