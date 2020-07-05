import random

n=int(input())
a=1
while(True):
            L = a
            R = n-L
            if '0' not in str(L) and '0' not in str(R):
                print([L,R])
                break
            a+=1
