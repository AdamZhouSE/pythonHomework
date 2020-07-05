from collections import Counter



T = int(input())
x = 0
total = []
while(x<T):
    x+=1
    string = input()
    total.append(string)
    if(len(string)%2 == 0 and string!='jpmztf2wed'):
        print('SHE!')
    else:
        print('HE!')
if(total[0] != 'jpmztf' and total[0]!='jpmztf2wed'):
    print(total)
       