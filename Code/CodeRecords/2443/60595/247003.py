def Test():
    nums=(str(x) for x in eval(input()))
    nums=sorted(nums)
    line=[]
    n=len(nums)
    i=-1
    count=0
    while(len(line)!=n):
        if(len(nums[i])==2):
            if(int(nums[i][1])>int(nums[i][0])):
                line.append(nums[i])
                save = i
                if (count != 0):
                    while (count != 0):
                        i = i + 1
                        line.append(nums[i])
                        count = count - 1
                    i = save
                i = i - 1
            else:
                count = count + 1
                i = i - 1
        elif(len(nums[i])==1):
            line.append(nums[i])
            save=i
            if(count!=0):
                while(count!=0):
                    i=i+1
                    line.append(nums[i])
                    count=count-1
                i=save
            i=i-1
    print("".join(line))
if __name__ == "__main__":
    Test()