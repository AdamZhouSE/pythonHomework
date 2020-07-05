def Test():
    n,m=map(int,input().split())
    citys=[]
    for i in range(m):
        citys.append(eval("["+input().strip().replace(" ",",")+"]"))
    sum=[]
    for i in range(len(citys[0])):
        people=0
        for j in range(len(citys)):
            people=people+citys[j][i]
        sum.append(people)
    winner1=sum.index(max(sum))+1
    do=[]
    for i in range(0,n):
        do.append(0)
    for i in range(len(citys)):
        temp=citys[i].index(max(citys[i]))
        do[temp]=do[temp]+1
    winner2=do.index(max(do))+1
    print(winner1 if winner1==winner2 else winner2)
if __name__ == "__main__":
    Test()