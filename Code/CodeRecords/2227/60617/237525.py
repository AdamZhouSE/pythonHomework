import sys
import math
def main():
    n=int((sys.stdin.readline()))
    k=int(sys.stdin.readline())
    result =[]
    lookup = [result]
    def dfs(node):
        for i in map(str, range(k)):
            nei=node+i
            if nei not in lookup:
                lookup.append(nei)
                dfs(nei[1:])
                result.append(i)

    dfs("0" * int(n-1))
    result="".join(result)+(n-1)*"0"

    print(result)
if __name__  =='__main__':
    main()