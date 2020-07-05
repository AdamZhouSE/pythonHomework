a=input().lstrip('[').rstrip(']').split(',')
i=0
while i<len(a) :
    if a[i]!=a[i+1]:
        print(a[i])
        break;
    i=i+2;