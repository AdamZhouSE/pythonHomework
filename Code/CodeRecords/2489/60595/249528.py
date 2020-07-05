from itertools import combinations
def Test():
    x=eval(input())
    lower=int(input())
    upper=int(input())
    a=[]
    for i in range(1,len(x)+1):
        a=a+(list(combinations(x,i)))
    count=0
    for k in a:
        if(sum(k)>=lower and sum(k)<=upper):
            count=count+1
    print(count)

if __name__ == "__main__":
    Test()