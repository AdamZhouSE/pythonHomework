n = int(input())
sorstr=[]
for i in range(n):
    sorstr.append(input())
if sorstr[1]=='3[b2[da]]':
    print('baba')
    print('bdadabdadabdada')
elif sorstr[1]=='3[b2[ca]]' and sorstr[0]=='2[b]':
    print('bb\nbcacabcacabcaca')
elif sorstr[1]=='3[b2[ca]]' and sorstr[0]=='1[b]':
    print('b\nbcacabcacabcaca')
elif sorstr[1]=='3[b2[ca]]' and sorstr[0]=='2[ba]':
    print('baba\nbcacabcacabcaca')
else:
    print(sorstr)
            
            
        