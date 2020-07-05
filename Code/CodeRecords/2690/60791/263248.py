def solve(s1,s2,index):
    count = 0
    for i in range(len(s1)):
        if (s1[i] == s2[index] and index!=len(s2)-1):
            count+=solve(s1[i+1:],s2,index+1)
        elif(s1[i] == s2[index] and index!=len(s2)-1):
            count+=1
    return count


T = int(input())
x = 0
while(x<T):
    x+=1
    n = input()
    arr = [input().split(' ')]
    print(solve(arr[0],arr[1],0))
        