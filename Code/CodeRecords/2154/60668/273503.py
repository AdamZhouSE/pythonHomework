def nums_27_Str(n):
    Str_1 = "".join(str(n))
    Str_2 = "".join(reversed(str(n)))
    return Str_1==Str_2
if __name__=='__main__':
    n = int(input())
    print(nums_27_Str(n))