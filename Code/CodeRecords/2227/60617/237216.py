import sys
import math
def main():
   n=int(sys.stdin.readline())
   k=int(sys.stdin.readline())
   Total=int(math.pow(k, n))
   AllinStr=""
   Keyword=[]
   while len(AllinStr)<n:
       AllinStr=AllinStr+"0"
   Keyword.append(AllinStr)
   while len(Keyword)<Total-1:
       for i in range(0, k):
            if AllinStr[len(AllinStr)-n+1:len(AllinStr)]+str(i) in Keyword:
                continue
            else:
                isAvailable=False
                for j in range(0, k):
                    if AllinStr[len(AllinStr)-n+2: len(AllinStr)]+str(i)+str(j) not in Keyword:
                        isAvailable=True
                if isAvailable:
                    AllinStr=AllinStr+str(i)
                    Keyword.append(AllinStr[len(AllinStr)-k:len(AllinStr)])
   for i in range(0, k):
        if AllinStr[len(AllinStr) - n + 1:len(AllinStr)] + str(i) in Keyword:
            continue
        else:
            AllinStr = AllinStr + str(i)
            Keyword.append(AllinStr[len(AllinStr) - k:len(AllinStr)])

   print(AllinStr)

if __name__  =='__main__':
    main()
