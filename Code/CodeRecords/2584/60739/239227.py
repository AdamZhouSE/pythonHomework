def judgeNim(num):
    if num % 4 == 0:
        return False
    else:
        return True
    
if __name__ == '__main__':
    nums = int(input());
    a = judgeNim(nums);
    print(a);
