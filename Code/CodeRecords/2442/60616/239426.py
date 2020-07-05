a=input()
items=eval(a)
items.sort()
if(len(items)<2):
    print(0)
else:
    arr=[]
    for j in range (1,len(items)):
        arr.append(abs(int(items[j])-int(items[j-1])))
    print(max(arr))