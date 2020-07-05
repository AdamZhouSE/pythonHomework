input=input()
ini=input[5:].index('"')
s=input[5:ini+5]
ini=input[6+ini:].index('"')+ini+6
step=input[ini+1:].index('"')
t=input[ini+1:step+ini+1]
arr1=list(s)
arr2=list(t)
if len(arr1)!=len(arr2):
    print('false')
else:
    arr1=sorted(arr1)
    arr2=sorted(arr2)
    if arr1==arr2:
        print('true')
    else:
        print('false')