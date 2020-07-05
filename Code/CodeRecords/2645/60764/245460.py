import math
bananas=list(eval(input()))
h=int(input())
k=int(min(bananas)/int(h/len(bananas)))
while True:
    i,j=0,0
    while i<=h and j<len(bananas):
        i=i+math.ceil(bananas[j]/k)
        j+=1
    if i<=h:
        break
    k+=1
print(k)