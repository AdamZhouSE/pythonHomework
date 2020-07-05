def Test():
    nums=(str(x) for x in eval(input()))
    nums=sorted(nums,reverse=True)
    print("".join(nums))
if __name__ == "__main__":
    Test()