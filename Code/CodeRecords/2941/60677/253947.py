n=int(input())
string=list(input())
answer=0
for i in string:
    if i=="A":
        answer+=4
    elif i.__eq__("B"):
        answer+=3
    elif i.__eq__("C"):
        answer+=2
    elif i.__eq__("D"):
        answer+=1
    else:
        answer+=0
print(answer/n)