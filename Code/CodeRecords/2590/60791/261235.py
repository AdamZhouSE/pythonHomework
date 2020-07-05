from collections import Counter



T = int(input())
x = 0
while(x<T):
    x+=1
    string = input()
    if(len(dict(Counter(string)))%2 == 0):
        print('SHE!')
    else:
        print('HE!')
       