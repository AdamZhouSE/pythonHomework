arr1=input().strip("[")
arr1=arr1.strip("]")
list1=arr1.split(",")
s1=[]
for ele in list1:
    if(ele!="null" and ele!=''):
        s1.append(int(ele))
arr2=input().strip("[")
arr2=arr2.strip("]")
list2=arr2.split(",")
s2=[]
for ele in list2:
    if(ele!="null" and ele!=''):
        s2.append(int(ele))
s3=s1+s2
print(sorted(s3))
