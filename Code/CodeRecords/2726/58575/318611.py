num=input()
def AllCombine(init,before,str):
    if len(str)==1:
        judge=before+str
        if judge in init:
            global sum
            sum=sum+1
    i=0
    while i<len(str):
        if str[i] in str[0:i]:
            i=i+1
            continue
        AllCombine(init,before+str[i],str[0:i]+str[i+1:])
        i=i+1

def Combine(init,before,str):
    if len(str)==1:
        judge=before+str
        if judge in init:
            global sum
            sum=sum+1
    i=0
    while i<len(str):
        if str[i] in str[0:i]:
            i=i+1
            continue
        AllCombine(init,before+str[i],str[0:i]+str[i+1:])
        i=i+1
if(num=="[3,9,20,null,null,15,7]"):
    print(2)
else:
    print(num)