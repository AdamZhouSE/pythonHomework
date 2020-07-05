from itertools import combinations
def Test():
    k,n=map(int,input().split(","))
    line=[1,2,3,4,5,6,7,8,9]
    result=[]
    for i in range(0,len(line)):
        result += list(combinations(line, i))
    result = [x for x in result if len(x) == k]
    a = []
    for j in result:
        if (sum(j) == n):
            a.append(list(j))
    print(a)

if __name__ == "__main__":
    Test()