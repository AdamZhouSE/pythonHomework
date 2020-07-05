def sort_1_split(list=[]):
    ans = maxN = 0
    for i,x in enumerate(list):
        maxN = max(maxN,x)
        if maxN==i:
            ans+=1
    print(ans)
if __name__=='__main__':
    list = eval(input())
    sort_1_split(list)