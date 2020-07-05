n = input()
left = int(n)-pow(10,len(n)-1)
big = int(n)-left
ls1 = list(str(left))
ls2 = list(str(big))
while '0' in ls1 or '0' in ls2:
    left+=1
    big-=1
    ls1 = list(str(left))
    ls2 = list(str(big))
print([big,left])