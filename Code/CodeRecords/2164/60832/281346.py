All = int(input())

for q in range(0, All):
    s=input()
    diff=set(s)

    print(len(s)-len(diff))