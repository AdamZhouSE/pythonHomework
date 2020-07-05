def solution(string):
    diffString=set(string)
    result=len(string)-len(diffString)
    return result
t=int(input())
for i in range(t):
    string=input()
    string=[i for i in string]
    print(solution(string))