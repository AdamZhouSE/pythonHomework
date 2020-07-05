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
def order(arr):
    arr=sorted(arr)
    element=list(set(arr))
    brr=[[v,arr.count(v)] for v in element]
    for i in range(len(brr)):
        for j in range(i,len(brr)):
            if brr[i][1]<brr[j][1] or (brr[i][1]==brr[j][1] and brr[i][0]>brr[j][0]):
                brr[i],brr[j]=brr[j],brr[i]
    string=''
    for v in brr:
        s=str(v[0])+' '
        for i in range(v[1]):
            string+=s
    return string

t=int(input())
for i in range(t):
    n=input()
    arr=nums(input())
    answer=order(arr)
    answer=answer
    print(answer)