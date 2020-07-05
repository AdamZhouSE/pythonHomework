import numpy as np
def examZero(string):
    i=len(string)-1;
    count=0;
    while(i>=0):
        if(string[i]=='0'):
            count+=1;
        else:
            break;
        i-=1;
    return count;

def Ffactorial(x):
    i=0;
    count=0;
    while(True):
        if(examZero(str(np.math.factorial(i)))==x):
            count+=1;
        elif(examZero(str(np.math.factorial(i)))>x):
            break;
        i+=1;
    print(count);

x=int(input());
Ffactorial(x);