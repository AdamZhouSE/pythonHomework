T=int(input())
for i in range(T):
    string=input()
    num=[0]*6
    num[0]=string.count('{')
    num[1]=string.count('[')
    num[2]=string.count('(')
    num[3]=string.count('}')
    num[4]=string.count(']')
    num[5]=string.count(')')
    if num[0]==num[3] and num[1]==num[4] and num[2]==num[5]:
        print('balanced')
    else:
        print('not balanced')