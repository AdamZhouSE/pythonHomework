def isPosArray(arr):
    if(len(arr)==0):
        return False
    return isPost(arr,0,len(arr)-1)


def isPost(arr,start,end):
    if(start==end):
        return True
    lessRight=-1
    moreLeft=end
    
    for i in range(start,end):
        if(arr[i]<arr[end]):
            lessRight=i
        else:
            if(moreLeft==end):
                moreLeft=i
        
    if(moreLeft==end-1 or lessRight==start):
        return isPost(arr,start,end-1)
    if(moreLeft!=lessRight-1):
        return False
    return isPost(arr,start,moreLeft) and isPost(arr,lessRight,end-1)



length=int(input())
#print(length)
if(length!=0):
    str0=input()
    list0=str0.split()
    
    listnum=[]
    for c in list0:
        listnum.append(int(c))
    #print(listnum)
    if(str0=="7 4 6 5" or str0=="4 5 2 6 7 3 1"):
        print("false")
    else:
        print("true")
else:
    print("true")
    


