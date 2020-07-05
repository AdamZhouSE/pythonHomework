def getInput():
    line = int(input());
    matrix_a = []

    for i in range (line):
        nums_str = input()
        nums = [int(n) for n in nums_str.split(",")];
        matrix_a.append(nums)

    return matrix_a;

def isValid(matrix, target):

    for i in range (len(matrix)):
        if matrix[i][0] <= target and matrix[i][-1] >= target:
            if target in matrix[i]:
                return True

    return False

if __name__ == '__main__':
    matrix = getInput();
    target = int(input())
    a = isValid(matrix, target);
    print(a);
