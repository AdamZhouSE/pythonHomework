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
def find(arr):
    tar=[4,8,15,16,23,42]
    answer=0
    k=0
    if len(arr)==0:
        return answer
    else:
        for i in range(len(arr)):
            if arr[i]==tar[k]:
                tar[k]=-1
                k=k+1
            elif arr[i]!=tar[k] and max(tar)>0:
                answer+=1
            elif max(tar)<0:
                answer+=1
        return answer
n=int(input())
arr=nums(input())
answer=find(arr)
print(answer)