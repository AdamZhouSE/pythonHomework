def main():
    arr=input().split(", ")
    nums=eval(arr[0].split(" ")[2])
    k=int(arr[1].split(" ")[2])
    t=int(arr[2].split(" ")[2])
    for i in range(0,len(nums)-1):
        for j in range(i+1, len(nums)):
            if abs(nums[i]-nums[j])<=t and abs(i-j<=k):
                print("true")
                exit()
    print("false")
if __name__=='__main__':
    main()