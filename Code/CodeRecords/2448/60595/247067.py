def Test():
    papers=eval(input())
    h=len(papers)
    print(h)
def check(h,papers):
    count=0
    for i in range(0,len(papers)):
        if(papers[i]>=h):
            count=count+1
    if(count==h):
        return count
    else:
        return check(h-1,papers)

if __name__ == "__main__":
    Test()