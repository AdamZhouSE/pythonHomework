import sys
import math
def main():
    n=int(sys.stdin.readline())
    k=int(sys.stdin.readline())
    result = str(k - 1)* n
    lookup = [result]

    total = k ** n

    while len(lookup) < total:

        node = result[len(result) - n + 1:]

        for i in range(k):

               neighbor = node + str(i)

               if neighbor not in lookup:
                   lookup.append(neighbor)

                   result=result+(str(i))

                   break

    print(result)
if __name__  =='__main__':
    main()