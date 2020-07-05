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
    print(sum.index(max(sum))+1)
if __name__ == "__main__":
    Test()