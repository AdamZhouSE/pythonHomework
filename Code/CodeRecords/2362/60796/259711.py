import math
n=int(input())
ls=[n]

i=1
while n>=2:
    n=n-1
    if i%4==1:
        ls.append("*")
    if i%4==2:
        ls.append("/")
    if i%4==3:
        ls.append("+")
    if i%4==0:
        ls.append("-")
    ls.append(n)
    i=i+1
print(ls)
while  ls.__contains__("*") or ls.__contains__("/"):
    i=0
    while i<len(ls)-1:
        if ls[i]=="*":
            t=ls[i-1]*ls[i+1]
            ls=ls[:i-1]+[t]+ls[i+2:]
            i=i-1
        if ls[i]=="/":
            t=math.floor(ls[i-1]/ls[i+1])
            ls=ls[:i-1]+[t]+ls[i+2:]
            i=i-1
        i=i+1

while ls.__contains__("+") or ls.__contains__("-"):
    i = 0
    while i < len(ls) - 1:
        if ls[i] == "+":
            t = ls[i - 1] + ls[i + 1]
            ls = ls[:i - 1] + [t] + ls[i + 2:]
            i = i - 1
        if ls[i] == "-":
            t = math.floor(ls[i - 1] - ls[i + 1])
            ls = ls[:i - 1] + [t] + ls[i + 2:]
            i = i - 1
        i = i + 1

print(ls[0])


