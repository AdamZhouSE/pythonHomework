import sys
def main():
   left=int(sys.stdin.readline())
   right=int(sys.stdin.readline())
   result=[]
   SelfDivSign=True
   for number in range(left,right+1):
       StrNum=str(number)
       for num in StrNum:
           if num=="0":
               break
           if number%int(num)!=0:
               SelfDivSign=False
               break
       if SelfDivSign:
           result.append(number)
   print(result)
if __name__  =='__main__':
    main()