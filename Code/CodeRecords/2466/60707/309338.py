
def triangleCount(S):
    # write your code here
    if len(S) < 3:
        return;
    count = 0;
    len1 = len(S)
    for i in range(0, len1 - 2):
        for j in range(i + 1, len(S) - 1):
            for z in range(j + 1, len(S)):
                if tri(S[i], S[j], S[z]) == 1:
                    #print(S[i], S[j], S[z])
                    count += 1
    return count


def tri(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return 1
    else:
        return 0


if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        k = int(input())
        temp2 = input().split(" ")
        for j in range(len(temp2)):
            temp2[j] = int(temp2[j])    
        r1 = triangleCount(temp2)
        print(r1)