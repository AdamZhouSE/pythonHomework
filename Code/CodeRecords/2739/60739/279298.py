from itertools import combinations

def getInput():
    input_str = input();
    nums = [int(n) for n in input_str.split(",")];
    return nums;

def num(k,n):
    nums=[1,2,3,4,5,6,7,8,9]
    res=[]
    for i in range(len(nums)):
        res +=list(combinations(nums,i))
    res=[x for x in res if len(x) == k]
    a=[]
    for j in res:
        if sum(j) ==n :
            a.append(list(j))
    return a

l = getInput()
print(num(l[0],l[1]))