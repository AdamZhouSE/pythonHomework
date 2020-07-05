def Test(nums,k,x):
    result=[]
    try:
        index=nums.index(x)
        if(index==0):
            result=nums[0:k]
        elif(index==len(nums)-1):
            result=nums[len(nums)-k:len(nums)]
        else:
            p1=nums[0:index+1]
            p2=nums[index+1:]
            i=-1
            j=0
            while(len(result)!=k):
                if(near(i,j,p1,p2,x)):
                    result.append(p1[i])
                    i=i-1
                else:
                    result.append(p2[j])
                    j=j+1
            result.sort()
    except:
        nums.append(x)
        nums.sort()
        result=Test(nums,k+1,x)
        result.remove(x)
    return result

def near(i,j,p1,p2,x):
    if(abs(p1[i]-x)<=abs(p2[j]-x)):
        return True
    else:
        return False

if __name__ == "__main__":
    nums = eval(input())
    k = int(input())
    x = int(input())
    result=Test(nums,k,x)
    print(result)