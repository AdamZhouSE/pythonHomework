str=input()
arr=eval(str[str.find("["):str.find("]")+1])
k=eval(str[str.find("k")+4:str.find("k")+5])
t=eval(str[str.find("t")+4:str.find("t")+5])
i=j=istrue=0
for i in range(0,len(arr)):
    if istrue==1:break
    for j in range(max(i-k,0),i):
        if abs(arr[i]-arr[j])<=t:
            print("true")
            istrue=1
            break
if(istrue==0):print("false")