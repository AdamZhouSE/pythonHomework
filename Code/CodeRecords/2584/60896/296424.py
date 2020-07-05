def find(a):
    if(a<4): return True
    if(a==4): return False
    i=int((a-4)/3)
    de=False
    if(i%2==0):de=True
    if(de):
        if((a-4)%3!=0): return True
        return False
    else:
        if((a-4)%3!=0): return False
        return True
    

a=eval(input())
print(find(a))
