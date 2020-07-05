arr=input().split(" ")
arr1=list(set(arr))
num=[]
for i in arr1:
    num.append(arr.count(i))
num.sort()
if len(arr1)>3:
    print("Alien")
elif len(arr1)==3:
    if num[len(num)-1]==4 or num[len(num)-1]==5:
        print("Bear")
else:
    if 4 in num or num[len(num)-1]==6:
        print("Elephant")
