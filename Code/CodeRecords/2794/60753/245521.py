import sys
import re
import math
s=sys.stdin.read()
digits=re.findall(r"\d+",s)
listline= [int(e) for e in digits ]
n=listline[0] 
del(listline[0])
booksearch=[]
booksearch.append([1,listline[0]])
total=listline[0]
for i in range(1,n):
    booksearch.append([total+1,total+listline[i]])
    total+=listline[i]
booknum=listline[n]
for i in range(booknum):
    book=listline[i+n+1]
    level=1
    for j in range(n):
        if book>=booksearch[j][0] and book<=booksearch[j][1]:
            break
        level+=1
    print(level)

                 