n=int(input())
string=input().strip()
result=""

for item in string:
    temp=chr(ord(item)+n if ord('A')<=ord(item)+n<=ord('Z') or ord('a')<=ord(item)+n<=ord('z') else ord(item)+n-26)

    result+=temp


print(result,end="")