import json
string=input()
arr1=json.loads(string)
arr2=eval(input())
arr1+=arr2
for element in arr1:
    if element==None:
        arr1.remove(None)
print(sorted(arr1))