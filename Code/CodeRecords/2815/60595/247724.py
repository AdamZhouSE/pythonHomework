def Test():
    x=int(input())
    nums=eval("["+str(input()).strip().replace(" ",",")+"]")
    sum=0
    for num in nums:
        sum=sum+abs(num-1)
    print(sum)
if __name__ == "__main__":
    Test()