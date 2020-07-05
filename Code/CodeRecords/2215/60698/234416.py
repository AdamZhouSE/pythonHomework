a=input()
a=a.split(',')
result=a[0];
if(len(a)>1):
    if(len(a)==2):
        result=result+'/'+a[1];
    else:
        result=result+'/('+a[1];
        for i in range(2,len(a)):
            result=result+'/'+a[i];
        result=result+')'
print(result)