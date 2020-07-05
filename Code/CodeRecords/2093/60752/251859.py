def arrange(lst,predix,eles,add):
    savepre=predix
    for i in range(len(lst)):
        predix=savepre+str(lst[i])
        nl=list(lst).copy()
        nl.remove(lst[i])
        if len(predix)==len(eles):
            add.append(predix)
        else:
            arrange(nl,predix,eles,add)





eles=[i for i in range(1,int(input())+1)]
k=int(input())
add=[]
ele=eles.copy()
arrange(ele,'',eles,add)
print(add[k-1])

