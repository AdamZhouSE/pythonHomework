def Test():
    s=input().replace(" ","")
    nums=eval(s[s.find("["):s.find("]")+1])
    k=eval(s[s.find("k")+2])
    t= eval(s[s.find("t") + 2])
    print(str(do(nums,k,t)).lower())
def do(nums,k,t):
    for i in range(0,len(nums)):
        for j in range(0,len(nums)):
            if(i!=j):
                if(abs(i-j)<=k) and (abs(nums[i]-nums[j])<=t):
                    return True
    return False

if __name__ == "__main__":
    Test()
