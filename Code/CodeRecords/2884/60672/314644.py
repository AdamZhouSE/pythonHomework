def nums(string):
    num='0123456789'
    nums=[]
    i=0
    while i<len(string):
        midstring=''
        k=0
        for j in range(i,len(string)):
            if string[j] in num:
                midstring+=string[j]
                k=k+1
            else:
                break
        if midstring!='':
            nums.append(int(midstring))
            midstring=''
            i=i+k
        else:
            i=i+1
            continue
    return nums
string1=input()
nd=nums(string1)
n,d=nd[0],nd[1]
arr=input()
arr=nums(arr)
answer=0
for i in range(len(arr)):
    for j in range(len(arr)):
        if abs(arr[i]-arr[j])<=d and i!=j:
            answer+=1
print(answer)