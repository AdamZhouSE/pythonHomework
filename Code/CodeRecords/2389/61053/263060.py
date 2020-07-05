def swap(lst,i):
    temp = lst[i]
    lst[i] = lst[i+1]
    lst[i+1] = temp

def wave_array(lst):
    i = 0
    while i < len(lst)-1:
        swap(lst,i)
        i = i + 2

if __name__  == "__main__":
    testNO = int(input())
    ans = []
    for i in range(0,testNO):
        n = int(input())
        lst = list(map(int,input().split()))
        wave_array(lst)
        ans.append(lst)
    for list in ans:
        print(*list)