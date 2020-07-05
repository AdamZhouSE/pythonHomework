def find(w,list):
    for x in list:
        if int(x) == int(w):
            list.remove(x)
            return True
    return False

problems = int(input())
for p in range(problems):
    size = int(input())
    A = input().split(" ")
    B = input().split(" ")
    
    judge = 1
    for x in A:
        if not find(x,B):
            judge = 0
            break
    print(judge)