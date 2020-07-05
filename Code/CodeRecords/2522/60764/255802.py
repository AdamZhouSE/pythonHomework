import numpy as np
arr1=list(eval(input()))
arr2=list(eval(input()))
nia2=[]
ia2=[]
for i in range(len(arr1)):
    if arr1[i] not in arr2:
        nia2.append(arr1[i])
    else:
        if len(ia2)==0:
            ia2.append(arr1[i])
        else:
            ind=arr2.index(arr1[i])
            check=True
            for j in range(len(ia2)):
                if arr2.index(ia2[j])>=ind:
                    ia2.insert(j,arr1[i])
                    check=False
                    break
            if check:
                ia2.append(arr1[i])
nia2.sort()
print(list(np.append(ia2,nia2)))