def Test():
    papers=eval(input())
    papers.sort()
    h = 0
    i=len(papers)
    while(i>=0):
        if (papers[i] >= h + 1):
            h=h+1
        else:
            break
        i=i-1
    print(h)

if __name__ == "__main__":
    Test()