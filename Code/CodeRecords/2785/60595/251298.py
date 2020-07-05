import itertools
def Test():
    n=int(input())
    nums=[]
    line=[]
    for i in range(0,n):
        temp=int(input())
        nums.append(temp if temp<=180 else 360-temp)
        line.append(-1)
        line.append(1)
    if(n>10):
        print("YES")
    else:
        totals=list(set(collect(n,line)))
        print(check(totals,nums))
def collect(n,line):
    return list(itertools.combinations_with_replacement(line,n))
def check(totals,nums):
    for x in totals:
        temp=list(x)
        result=0
        for i in range(0,len(temp)):
            result=result+nums[i]*temp[i]
        if(result==0):
            return "YES"
    return "NO"
if __name__ == "__main__":
    Test()