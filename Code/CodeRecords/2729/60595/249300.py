def Test():
    nums=eval(input())
    find=0
    for k in nums:
        find=find^k
    print(find)

if __name__ == "__main__":
    Test()