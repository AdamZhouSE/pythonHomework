def peers(d,heights):
    heights.sort()
    cnt=0
    for i in range(len(heights)-1):
        for j in range(i+1,len(heights)):
            if heights[j]-heights[i]<=d:
                cnt+=1
            else:
                break
    return cnt*2

if __name__=="__main__":
    n,d=input().split()
    n=int(n)
    d=int(d)
    heights=input().split()
    heights=[int(x) for x in heights]
    ans=peers(d,heights)
    print(ans)