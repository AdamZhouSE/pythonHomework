list =input()
res=[]
def num(i,list):
    n=0
    for j in range(len(list)):
        if int(list[j])>=i:
            n+=1
    if n>=i:
        return True
    else:
        return False
for i in range(1,len(list)+1):
    if num(i,list):
        res.append(i)

print(res[len(res)-1])