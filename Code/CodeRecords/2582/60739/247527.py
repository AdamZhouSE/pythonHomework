def getInput():
    nums_str = input()
    nums = [int(n) for n in nums_str.split(",")];
    return nums

def getMax(arr1, arr2):
    max = 0
    for i in range (len(arr1)):
        for j in range (len(arr2)):
            a = abs(arr1[i] - arr1[j])
            b = abs(arr2[i] - arr2[j])
            c = abs(i - j)
            if a + b + c >= max:
                max = a + b + c
                
    return max

if __name__ == '__main__':
    arr1 = getInput();
    arr2 = getInput();
    a = getMax(arr1, arr2);
    print(a);
