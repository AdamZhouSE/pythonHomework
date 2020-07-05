def Test():
    nums=eval(input())
    k=int(input())
    x=int(input())
    index=nums.index(x)
    if(index!=-1):
        if(index==0):
            print(nums[0:k])
            return
        elif(index==len(nums)-1):
            print(nums[len(nums)-k:len(nums)])
            return
        else:
            result=[]
            result.append(x)
            p1=nums[0:index]
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
            print(result)

def near(i,j,p1,p2,x):
    if(abs(p1[i]-x)<=abs(p2[j]-x)):
        return True
    else:
        return False

if __name__ == "__main__":
    Test()