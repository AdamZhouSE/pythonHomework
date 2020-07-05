def quanpailie(arr,position,end,oc)->list:
    if position==end:
        str=""
        for index in range(len(arr)):
            str=str+arr[index]
        oc.append(str)
    else:
        for index in range(position,end):
            arr[index], arr[position] = arr[position], arr[index]
            quanpailie(arr, position + 1, end,oc)
            arr[index], arr[position] = arr[position], arr[index]
    return oc

def panduan(a:int)->bool:
    if a == 1:
        return True
    elif a%2==1:
        return False
    else:
        return panduan(a/2)

a = (list)(input())
oc=[]
oc=quanpailie(a,0,len(a),oc)
x=False
for index in range(len(oc)):
    if oc[index][0]=="0":
        continue
    if panduan((int)(oc[index])):
        x=True
if x:
    print("true")
else:
    print("false")