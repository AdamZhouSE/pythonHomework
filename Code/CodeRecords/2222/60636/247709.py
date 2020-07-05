source=input().split("=")
left=list(source[0])
right=list(source[1])
lefts=[]
rights=[]
left_a=0
left_start=0
right_a=0
right_start=0
while(left_a<len(left)):
    if((left_a==0)&(left[left_a]=="-")):
        left_a=left_a+1
    elif((left[left_a]=="+")|(left[left_a]=="-")):
        res=""
        for i in left[left_start:left_a]:
            res=res+i
        if(left[left_a-1]=="-"):
            res="-"+res
        lefts.append(res)
        left_a=left_a+1
        left_start=left_a
    else:
        left_a=left_a+1
res=""
for i in left[left_start:left_a]:
    res=res+i
if(left[left_a-1]=="-"):
    res="-"+res
lefts.append(res)
while(right_a<len(right)):
    if((right_a==0)&(right[right_a]=="-")):
        right_a=right_a+1
    elif((right[right_a]=="+")|(right[right_a]=="-")):
        res=""
        for i in right[right_start:right_a]:
            res=res+i
        if(right[right_a-1]=="-"):
            res="-"+res
        rights.append(res)
        right_a=right_a+1
        right_start=right_a
    else:
        right_a=right_a+1
res=""
for i in right[right_start:right_a]:
    res=res+i
if(right[right_a-1]=="-"):
    res="-"+res       
rights.append(res)
print(lefts)
print(rights)
x=[]
number=[]
for i in lefts:
    if(i.isdigit()):
        number.append(-int(i))
    else:
        y=list(i)
        y.pop(-1)
        if(len(y)==0):
            x.append(1)
        elif(y[0]=="-"):
            res=""
            for a in y[1:]:
                res=res+a
            x.append(-int(res))
        else:
            res=""
            for a in y:
                res=res+a
            x.append(int(res))
print(x)
print(number)