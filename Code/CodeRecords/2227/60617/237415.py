import sys
import math
def main():
    n=(sys.stdin.readline())
    k=(sys.stdin.readline())
    result ="0"* n
    lookup = [result]
    total = k ** n
    def dfs(node):
        for i in map(str, range(k)):
            nei=node+i
            if nei not in lookup:
                lookup.append(nei)
                dfs(nei[1:])
                result=result+i
                
    dfs(result)
    print(result)
if __name__  =='__main__':
    main()

                   break

    print(result)
if __name__  =='__main__':
    main()