res=True;
numslist=eval("["+input()+"]");
for i in range(len(numslist)):
    for j in range(i+2,len(numslist)):
        if(numslist[i]>numslist[j]):
            res=False;
if(res):
    print("True")
else:print("False")