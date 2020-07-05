t = int(input())
for i in range(t):
    n = int(input())
    grades = [int(i) for i in input().split(" ")]
    grades.sort()
    if n%2 == 0:
        print(int((grades[n//2-1]+grades[n//2])//2))
    else:
        print(grades[n//2])