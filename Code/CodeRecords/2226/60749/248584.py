lower=int(input())
upper=int(input())
def judgenumber(num):
    num_str=str(num)
    if "0" in num_str:
        return False
    temp=[]
    for x in num_str:
        temp.append(int(x))
    
    for h in temp:
        if not num%h==0:
            return False
    return True
res=[]
for x in range(lower, upper+1):
    if judgenumber(x):
        res.append(x)
print(res)