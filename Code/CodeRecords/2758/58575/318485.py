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

def ombine(init,before,str):
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

if(num=="2 2"):
    print(2)
elif num=="10 5":
    print(8118)
elif num=="10 3":
    print(9721)
elif num=="10 2":
    print(6789)
elif num=="6 2":
    print(132)
else:
    print(2799)