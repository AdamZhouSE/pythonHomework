n=int(input())
def findPairs(array):
    sumPair=dict()
    n=len(array)
    i=0
    while i<n:
        j=i+1
        while j<n:
            sums=array[i]+array[j]
            if sums not in sumPair:
                sunPair[sums]=pair(i,j)
for i in range(n):
    N=int(input())
    string=input()
    try:
        num_list=list(map(int,string.split()))
    except:
        num_list=list(map(int,string.split(",")))
        