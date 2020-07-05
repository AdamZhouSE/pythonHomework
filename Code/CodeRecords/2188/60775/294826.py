inp1 = input().split(' ')
leng = int(inp1[0])
K = int(inp1[1])
str1 = input()
str2 = input()
nums_of_que = int(input())
for e in range(nums_of_que):
    input2 = input().split(' ')
    begin1 = int(input2[0])
    end1 = int(input2[1])
    begin2 = int(input2[2])
    end2 = int(input2[3])
    sub1 = str1[begin1-1:end1]
    sub2 = str2[begin2-1:end2]
    visited = [False] * (len(sub1))
    result = 0
    for i in range(0,len(sub1)-len(sub2)+1):
        if visited[i:i+len(sub2)] == [False]*(len(sub2)) and sub1[i:i+len(sub2)] == sub2:
            result += K-(i+begin1)
            visited[i:i+len(sub2)] = [True]*(len(sub2))
    print(result)

