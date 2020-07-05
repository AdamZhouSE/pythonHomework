def func1(root1,root2):
    tmp=[]
    for i in root1:
        if i!="":
            tmp.append(i)
    for j in root2:
        if j!="":
            tmp.append(j)
    tmp.sort()
    print(tmp)
    
root1=eval(input().replace("null,","").replace("null",""))
root2=eval(input().replace("null","").replace("null",""))
func1(root1,root2)