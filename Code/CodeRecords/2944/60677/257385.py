expression=list(input())
n=expression.__len__()
re=expression[:].reverse()
left=0
right=0
def find(list,n):
    answer=[]
    try:
        for i in range(n):
            if list[i]=="(":
                answer.append("(")
            if list[i]==")":
                answer.pop()
        if answer.__len__()!=0:
            return "NO"
        else:
            return "YES"

    except:
        return "NO"

print(find(expression,n),end="")