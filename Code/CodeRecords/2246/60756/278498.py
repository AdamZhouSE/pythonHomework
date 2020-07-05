import math
def get_two_list(n:int)->list:
    ans=[]
    x=1
    while x<=n:
        ans.append(sorted(list(str(x))))
        x*=2
    return ans

N=input()
n=10**(math.ceil(math.log(int(N),10)))
N=sorted(list(N))
arr=get_two_list(n)
print(N in arr)