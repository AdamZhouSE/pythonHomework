info=eval(input())
K=int(input())
dict={}
for y in info:
    if y not in dict.keys():
        dict[y]=1
    else:
        dict[y]=dict[y]+1
a=[k for k,v in dict.items() if v==K]
print(a[0])
    
        