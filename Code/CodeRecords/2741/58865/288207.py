lst=eval(input())

i=0
j=i
length=0
a=0
b=0
while(j<len(lst)-1):
    if lst[j+1]>lst[j]:
        j+=1
    else:
        if j-i>length:
            length=j-i
            b=j
            a=i
        i+=1
        j=i

print(len(lst[a:b+1]))