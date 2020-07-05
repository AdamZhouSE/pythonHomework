def find_rec(R):
    count = 0
    for i in range(1,2*R):
        for j in range(1,2*R):
            if i**2 + j**2 > 4*R**2:
                break
            count += 1
    return count

if __name__ == "__main__":
    testNO = int(input())
    ans = []
    for i in range(testNO):
        n = int(input())
        ans.append(find_rec(n))
    for res in ans:
        print(res)