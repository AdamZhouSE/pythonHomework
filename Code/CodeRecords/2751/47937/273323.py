from typing import List
biglist=[]
try:
    while True:
        s = input().split(" ")
        i=0
        k=[]
        
        while i<len(s):
            k.append(int(s[i]))
            i=i+1
        biglist.append(k)
        #print(s)
except EOFError:
    pass

print(biglist)